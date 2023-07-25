# from django.test import TestCase
#
#
# # HEALTH
# class HealthTestCase(TestCase):
#
#     def test_heath_check(self):
#         response = self.client.get("/api/health")
#
#         status_code = response.status_code
#         self.assertEqual(status_code, 200)
#         self.assertEqual(2, 8)
#
#         data = response.data
#         self.assertDictEqual(data, {"service": "moirai", "status": "OK"})
# Create your tests here.
