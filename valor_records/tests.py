from django.test import TestCase
from django.contrib.auth.models import User
from .models import ValorRecord, HouseType, Deanery


class ValorRecordModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.deanery = Deanery.objects.create(deanery_name='Test Deanery')
        self.house_type = HouseType.objects.create(house_type='Abbey')

    def test_slugify(self):
        valor_record = ValorRecord.objects.create(
            name='Test Monastery',
            record_type='Monastery',
            deanery=self.deanery,
            house_type=self.house_type,
            created_by=self.user
        )
        valor_record.save(user=self.user)
        self.assertEqual(valor_record.slug, 'test-monastery-abbey')
