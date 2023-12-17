from rest_framework import generics
from .models import Source, SourceUsers
from .serializers import SourceSerializer, SourceUsersSerializer
from .tasks import process_and_save_user_data
from users.models import User, Specialization, Skill
from rest_framework.response import Response
from django.db.models import Count
from api.models import Event
from rest_framework import status


class SourceListView(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.type == 'tg':
            process_and_save_user_data(instance.url)  # TODO database is locked, надо фиксить


class SourceUsersListView(generics.ListCreateAPIView):
    queryset = SourceUsers.objects.all()
    serializer_class = SourceUsersSerializer


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SourceUsers.objects.all()
    serializer_class = SourceUsersSerializer


def get_top_cities_with_total():
    top_cities = User.objects.exclude(city__isnull=True).exclude(city='').values('city') \
                     .annotate(count=Count('city')) \
                     .order_by('-count')[:10]
    total_users_with_city = User.objects.exclude(city__isnull=True).exclude(city='').count()

    return top_cities, total_users_with_city


class TopCitiesAPIView(generics.ListAPIView):
    def get(self, request, format=None):
        top_cities, total = get_top_cities_with_total()
        for city in top_cities:
            city['percentage'] = (city['count'] / total) * 100

        return Response({
            'total_users_with_city': total,
            'top_cities': top_cities
        })


def get_specializations_with_user_count():
    specializations_with_count = Specialization.objects.annotate(user_count=Count('users')).order_by('-user_count')
    total_users = User.objects.count()
    return specializations_with_count, total_users


def get_skills_with_user_count():
    skills_with_count = Skill.objects.annotate(user_count=Count('users')).order_by('-user_count')
    total_users = User.objects.count()
    return skills_with_count, total_users


class SkillAPIView(generics.ListAPIView):
    def get(self, request, format=None):
        skills, total_users = get_skills_with_user_count()
        data = {
            'total_users': total_users,
            'skills': [{'name': skill.name, 'user_count': skill.user_count} for skill in skills]
        }
        return Response(data)


class SpecializationAPIView(generics.ListAPIView):
    def get(self, request, format=None):
        specializations, total_users = get_specializations_with_user_count()
        data = {
            'total_users': total_users,
            'specializations': [{'name': spec.name, 'user_count': spec.user_count} for spec in specializations]
        }
        return Response(data)


def get_event_statistics():
    total_events = Event.objects.count()
    events_with_visitor_count = Event.objects.annotate(visitor_count=Count('participants'))
    visitor_count_by_type = Event.objects.values('event_type').annotate(total_visitors=Count('participants'))

    return {
        'total_events': total_events,
        'events': events_with_visitor_count,
        'visitor_count_by_type': visitor_count_by_type
    }


class EventStatisticsAPIView(generics.ListAPIView):
    def get(self, request, format=None):
        stats = get_event_statistics()
        return Response(stats)


def get_user_events(user_id):
    try:
        user = User.objects.get(pk=user_id)
        user_events = user.events_participated.all()
        return user_events
    except User.DoesNotExist:
        return None


class UserEventsAPIView(generics.ListAPIView):
    queryset = Event.objects.all()

    def get(self, request, user_id, format=None):
        user_events = get_user_events(user_id)
        if user_events is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        events_data = [{'title': event.title, 'event_type': event.event_type, 'start_time': event.start_time,
                        'end_time': event.end_time} for event in user_events]
        return Response(events_data)
