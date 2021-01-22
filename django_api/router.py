from employeapi.viewsets import EmployerViewset
from rest_framework import routers 

router=routers.DefaultRouter()
router.register('api/employee',EmployerViewset)
