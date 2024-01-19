"""
python manage.py shell
exec(open('dbscript.py').read())
"""
from payments.models import Item


Item(name="Shield", description="Good Shield", price="15").save()
Item(name="Stick", description="Good Stick", price="10").save()
Item(name="Stone", description="Good Stone", price="5").save()

print("all done")
quit()
