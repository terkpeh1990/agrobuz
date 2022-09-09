from django.urls import path


from .import views
from .import bio_data
from .import crop_faming
from .import animal_farming
from .import association
from .import business_registration
from .import land_info
from .import dashboard
from .import sysadmin
from .import audittrial


app_name = 'agric'

urlpatterns = [

    #bioData
    path('create_bio_data', bio_data.create_bio_data,name='create_bio_data'),
    path('Update_bio_data/<str:pk>/',bio_data.Update_bio_data,name='Update_bio_data'),
    path('manage_biodata',bio_data.manage_biodata,name='manage_biodata'),
    path('view_bio/<str:pk>/',bio_data.view_bio,name='view_bio'),
    path('Update_bio_profile_data/<str:pk>/',bio_data.Update_bio_profile_data,name='Update_bio_profile_data'),
    path('delete_biodata',bio_data.delete_biodata,name='delete_biodata'),
    path('delete_bio/<str:pk>/',bio_data.delete_bio,name='delete_bio'),

    #cropfarm
    path('create_crop_farming/<str:pk>/',crop_faming.create_crop_farming,name='create_crop_farming'),
    path('delete_crop_farming/<str:pk>/',crop_faming.delete_crop_farming,name='delete_crop_farming'),
    path('update_crop_farming/<str:pk>/',crop_faming.update_crop_farming,name='update_crop_farming'),
    path('create_profile_crop_farming/<str:pk>/',crop_faming.create_profile_crop_farming,name='create_profile_crop_farming'),
    path('update_profile_crop_farming/<str:pk>/',crop_faming.update_profile_crop_farming,name='update_profile_crop_farming'),

    #animalfarm
    path('create_animal_farming/<str:pk>/',animal_farming.create_animal_farming,name='create_animal_farming'),
    path('update_animal_farming/<str:pk>/',animal_farming.update_animal_farming,name='update_animal_farming'),
    path('delete_animal_farming/<str:pk>/',animal_farming.delete_animal_farming,name='delete_animal_farming'),
    path('create_profile_animal_farming/<str:pk>/',animal_farming.create_profile_animal_farming,name='create_profile_animal_farming'),
    path('update_profile_animal_farming/<str:pk>/',animal_farming.update_profile_animal_farming,name='update_profile_animal_farming'),

    #association
    path('create_association',association.create_association,name='create_association'),
    path('Update_association/<str:pk>/',association.Update_association,name='Update_association'),
    path('manage_association',association.manage_association,name='manage_association'),
    path('delete_association/<str:pk>/',association.delete_association,name='delete_association'),
    path('view_association/<str:pk>/',association.view_association,name='view_association'),

    #association/bio-association
    path('create_bio_association/<str:pk>/',association.create_bio_association,name='create_bio_association'),
    path('update_bio_association/<str:pk>/',association.update_bio_association,name='update_bio_association'),
    path('delete_bio_association/<str:pk>/',association.delete_bio_association,name='delete_bio_association'),
    path('add_association/<str:pk>/',association.add_association,name='add_association'),
    path('create_profile_bio_association/<str:pk>/',association.create_profile_bio_association,name='create_profile_bio_association'),
    path('update_profile_bio_association/<str:pk>/',association.update_profile_bio_association,name='update_profile_bio_association'),

    #Business
    path('create_business/<str:pk>/',business_registration.create_business,name='create_business'),
    path('update_business/<str:pk>/',business_registration.update_business,name='update_business'),
    path('delete_business/<str:pk>/',business_registration.delete_business,name='delete_business'),
    path('create_land_info/<str:pk>/',land_info.create_land_info,name='create_land_info'),
    path('create_partner/<str:pk>/',business_registration.create_partner,name='create_partner'),
    path('add_partner/<str:pk>/<str:bus>/',business_registration.add_partner,name='add_partner'),
    path('delete_partner/<str:pk>/',business_registration.delete_partner,name='delete_partner'),
    path('manage_business',business_registration.manage_business,name='manage_business'),
    path('view_business/<str:pk>/',business_registration.view_business,name='view_business'),
    path('create_profile_business/<str:pk>/',business_registration.create_profile_business,name='create_profile_business'),
    path('update_profile_business/<str:pk>/',business_registration.update_profile_business,name='update_profile_business'),
    path('agri_business_d',business_registration.agri_business_d,name='agri_business_d'),
    path('add_ic_code/<str:pk>/',business_registration.add_ic_code,name='add_ic_code'),
    path('delete_code/<str:pk>/',business_registration.delete_code,name='delete_code'),


    #dashboard
    path('home',dashboard.home,name='home'),

   #sysadmin
    path('manage_profiles',sysadmin.manage_profiles,name='manage_profiles'),
    path('reset_staff_password/<str:pk>/',sysadmin.reset_staff_password,name='reset_staff_password'),
    path('manage_grouping',sysadmin.manage_grouping,name='manage_grouping'),
    path('populate_grouping',sysadmin.populate_grouping,name='populate_grouping'),
    path('delete_grouping',sysadmin.delete_grouping,name='delete_grouping'),
    path('assign_grouping/<str:pk>/',sysadmin.assign_grouping,name='assign_grouping'),
    path('set_staff_group/<str:profileid>/<str:groups>/',sysadmin.set_staff_group,name='set_staff_group'),
    path('signup', views.signup, name="signup"),

   #Audit Trail and logs
   path('biotrail',audittrial.bioaudittrail,name='biotrail'),
   path('audittrail_view_bio/<str:history_id>/',audittrial.audittrail_view_bio,name='audittrail_view_bio'),
   path('userlogs',audittrial.userlogs,name='userlogs'),
   path('businessaudittrail',audittrial.businessaudittrail,name='businessaudittrail'),
   path('audittrail_view_business/<str:history_id>/',audittrial.audittrail_view_business,name='audittrail_view_business'),


]