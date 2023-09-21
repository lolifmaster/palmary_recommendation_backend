from rest_framework.routers import DefaultRouter
from products.views import ProductView, CategoryView, TypeView


app_name = 'products'

router = DefaultRouter()
router.register(r'product', ProductView, basename='product')
router.register(r'category', CategoryView, basename='category')
router.register(r'type', TypeView, basename='type')

urlpatterns = router.urls
