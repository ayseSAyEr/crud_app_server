from django.contrib import admin
from . models import Employee
from . models import Team
from . models import TeamEmployee

# for selecting foreignkey, TeamEmployeeAdmin class is generated 
class TeamEmployeeAdmin(admin.ModelAdmin):
    fields = ('employee_id', 'team_id', 'is_lead')

    # this selects and displays id value of Employee class in admin add page
    def get_form(self, request, obj=None, **kwargs):
        form = super(TeamEmployeeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['employee_id'].label_from_instance = lambda obj: "{} {}".format(obj.name, obj.surname)
        form.base_fields['team_id'].label_from_instance = lambda obj: "{}".format(obj.team_name)
        # form.base_fields['employee_id'].label_from_instance = lambda obj: "{} {} {}".format(obj.id, obj.name, obj.surname)
        return form


# add admin page models registration
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(TeamEmployee,TeamEmployeeAdmin)
