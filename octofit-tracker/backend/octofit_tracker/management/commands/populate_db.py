from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='captainamerica', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='password', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)
        brucew = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)
        diana = User.objects.create_user(username='wonderwoman', email='diana@dc.com', password='password', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='fly', duration=10, distance=100)
        Activity.objects.create(user=brucew, type='drive', duration=50, distance=30)
        Activity.objects.create(user=diana, type='run', duration=40, distance=8)

        # Create workouts
        Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel heroes')
        Workout.objects.create(name='Justice League Strength', description='Strength training for DC heroes')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
