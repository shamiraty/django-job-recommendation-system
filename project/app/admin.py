from django.contrib import admin
from .models import *
from django.utils.html import format_html
from import_export import resources  
from import_export.admin import ImportExportMixin
from django.contrib.auth.admin import UserAdmin


 

#avoid default ID  when uploading csv and specify custom fields to upload  
class JobResource(resources.ModelResource):
    class Meta:
        model = Job
        fields = ("id","title", "description", "company", "location", "category", "created_date", "deadline", "salary","requirements","responsibilities","contact_email","required_skills","education_level")
        import_id_fields = ['id']  # Specify the field used as import identifier PK

    #def before_import_row(self, row, **kwargs):
        #row.pop('id', None)  # Exclude 'id' field from import
 
class JobAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class =JobResource
    list_display = ('title', 'company', 'location', 'category', 'created_date', 'deadline', 'salary',)
    list_filter = ('category', 'location', 'created_date')
    search_fields = ('title', 'description', 'company', 'requirements', 'responsibilities')
    list_per_page = 10
    list_max_show_all = 50
    list_editable=( 'category', )
    readonly_fields = ('created_date', 'image_tag')  # Assuming created_date shouldn't be editable
    date_hierarchy = 'created_date'
    # Pagination
    list_per_page = 10
    # Show image
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        else:
            return 'No Image'
    image_tag.short_description = 'Image'  # Displayed as column header in admin

admin.site.register(Job, JobAdmin)



@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'applied_on')
    list_per_page = 15
    list_filter = ( 'job', 'applied_on')  
    search_fields = ('user__username', 'job__title')
    list_editable=('job',)  
 
    
 

