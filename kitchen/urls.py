from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishCreateView,
    DishDeleteView,
    DishDetailView,
    DishUpdateView,

)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "dish_type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish_type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish_type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dish/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dish/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dish/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
]

app_name = "kitchen"
