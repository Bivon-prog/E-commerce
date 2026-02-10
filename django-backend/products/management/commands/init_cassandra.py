"""
Management command to initialize Cassandra keyspace and tables.
"""
from django.core.management.base import BaseCommand
from products.models import CassandraDB


class Command(BaseCommand):
    help = 'Initialize Cassandra keyspace and create tables'

    def handle(self, *args, **options):
        self.stdout.write('Initializing Cassandra...')
        
        try:
            CassandraDB.initialize_keyspace()
            self.stdout.write(self.style.SUCCESS('✓ Cassandra initialized successfully'))
            self.stdout.write(self.style.SUCCESS(f'✓ Keyspace created/verified'))
            self.stdout.write(self.style.SUCCESS(f'✓ Products table created/verified'))
            self.stdout.write(self.style.SUCCESS(f'✓ Indexes created/verified'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error initializing Cassandra: {str(e)}'))
            raise
