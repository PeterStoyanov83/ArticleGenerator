from django.core.management.base import BaseCommand
from ArticleGenerator.models import ArticleTopic


class Command(BaseCommand):
    help = 'Populates the database with predefined article topics'

    def handle(self, *args, **kwargs):
        topics = [
            "The Evolution of Guitar Design",
            "Acoustic vs. Electric: A Comprehensive Comparison",
            "The Impact of Wood Types on Guitar Sound",
            "Beginner's Guide to Guitar Maintenance",
            "How to Choose the Right Guitar for You",
            "Exploring Different Guitar Tunings",
            "The Science of Sound: How Guitars Produce Music",
            "Famous Guitarists and Their Preferred Instruments",
            "The Role of Guitars in Different Music Genres",
            "Innovations in Guitar Technology",
            "Sustainability in Guitar Manufacturing",
            "The Anatomy of a Guitar: A Deep Dive",
            "How to Amplify an Acoustic Guitar",
            "The Future of Guitars: Smart Guitars and IoT",
            "Guitar Playing Techniques Every Player Should Know",
            "The Influence of Guitars in Popular Culture",
            "How to Record Guitar Music at Home",
            "Understanding Guitar Pedals and Effects",
            "The Art of Guitar Customization",
            "Guitars and Music Therapy",
            "The Intersection of Guitars and Blockchain Technology",
            "Tips for Traveling with Your Guitar",
            "How to Shop for a Vintage Guitar",
            "The Importance of Proper Guitar Setup",
            "The Role of the Guitar in Jazz Music",
            "Exploring the World of Seven-String Guitars",
            "The Basics of Guitar Tablature",
            "How to Master Fingerstyle Guitar",
            "The Rise of Female Guitarists",
            "The History of the Classical Guitar",
            "How to Improve Your Guitar Solos",
            "The Guitar in Flamenco Music",
            "The Importance of Guitar Scales",
            "How to Choose Guitar Strings",
            "The Role of the Guitar in Country Music",
            "The Guitar and Music Education",
            "How to Read Guitar Sheet Music",
            "The Guitar in Heavy Metal",
            "The Basics of Guitar Amplification",
            "The Guitar in Blues Music",
            "How to Choose a Guitar Pick",
            "The Guitar in Folk Music",
            "The Importance of Guitar Lessons",
            "The Guitar in Reggae Music",
            "How to Care for Your Guitar's Fretboard",
            "The Guitar in Latin Music",
            "The Importance of Rhythm in Guitar Playing",
            "The Guitar in Indie Music",
            "How to Choose a Guitar Case",
            "The Guitar in Alternative Music",
            "The Importance of Guitar Intonation",
            "The Guitar in Punk Music",
            "How to Record Electric Guitar",
            "The Guitar in R&B Music",
            "How to Choose a Guitar Strap",
            "The Guitar in Hip-Hop Music",
            "The Importance of Guitar Action",
            "The Guitar in Electronic Music",
            "How to Choose a Guitar Amplifier",
            "The Guitar in Gospel Music",
            "The Importance of Guitar Truss Rod Adjustment",
            "The Guitar in Funk Music",
            "How to Record Acoustic Guitar",
            "The Guitar in Soul Music",
            "How to Choose a Guitar Capo",
            "The Guitar in Pop Music",
            "The Importance of Guitar Nut Adjustment",
            "The Guitar in Classical Music",
            "How to Mic a Guitar Amplifier",
            "The Guitar in Rock Music",
            "The Importance of Guitar Bridge Adjustment",
            "The Guitar in World Music",
            "How to Use a Loop Pedal",
            "The Guitar in Psychedelic Music",
            "How to Choose a Guitar Pedalboard",
            "The Guitar in Disco Music",
            "The Importance of Guitar Pickups",
            "The Guitar in Ska Music",
            "How to Use a Wah Pedal",
            "The Guitar in Grunge Music",
            "How to Choose a Guitar Tuner",
            "The Guitar in Shoegaze Music",
            "The Importance of Guitar Tone Woods",
            "The Guitar in Emo Music",
            "How to Use a Volume Pedal",
            "The Guitar in Post-Rock Music",
            "How to Choose a Guitar Cable",
            "The Guitar in Drone Music",
            "The Importance of Guitar Finish",
            "The Guitar in Ambient Music",
            "How to Use a Compressor Pedal",
            "The Guitar in Lo-fi Music",
            "How to Choose a Guitar Stand",
            "The Guitar in New Age Music",
            "The Importance of Guitar Inlays",
            "The Guitar in Chillout Music",
            "How to Use a Phaser Pedal",
            "The Guitar in Trance Music",
            "The Importance of Guitar Hardware"
        ]

        for title in topics:
            ArticleTopic.objects.create(title=title)
