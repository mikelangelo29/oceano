
from django.contrib.auth.mixins import UserPassesTestMixin


class StaffMixing(UserPassesTestMixin):
    """ solo lo staff può creare sezioni """
    
    def test_func(self):
      return self.request.user.is_staff