# 9-10. Imported Restaurant

from restaurant_module import Restaurant

my_restaurant = Restaurant("McDonald's", "American")
my_restaurant.describe_restaurant()


# 9-12. Multiple Modules

from admin_module import Admin

admin_user = Admin("Admin", "Mario")
admin_user.privileges.privileges = ["can edit user profiles", "can moderate comments"]
admin_user.privileges.show_privileges()