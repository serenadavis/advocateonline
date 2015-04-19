import xlwt
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.db.models import Sum
from .models import *

class InteractionInline(admin.TabularInline):
	model = Interaction
	extra = 0

def export_xls(modeladmin, request, queryset):
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=contacts.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Contacts")
    
    row_num = 0
    
    columns = [
        (u"Graduation year", 256*8),
        (u"Other degrees", 256*12),
        (u"Last name", 256*20),
        (u"First name", 256*20),
        (u"Middle name", 256*20),
        (u"Article", 256*10),
        (u"Title", 256*10),
        (u"Nick name", 256*20),
        (u"Address 1", 256*30),
        (u"Address 2", 256*30),
        (u"Address 3", 256*30),
        (u"City", 256*15),
        (u"State", 256*10),
        (u"Zip code", 256*12),
        (u"Country", 256*10),
        (u"Email 1", 256*30),
        (u"Email 2", 256*30),
        (u"Phone", 256*15),
        (u"Profession", 256*20),
        (u"Board", 256*20),
        (u"Position held", 256*20),
        (u"LinkedIn", 256*30),
        (u"Facebook", 256*30),
        (u"Website", 256*30),
        (u"Published work?", 256*30),
        (u"Category", 256*15),
        (u"Tier", 256*15),
        (u"Notes", 256*30)
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in queryset:
        row_num += 1
        row = [
            obj.graduationYear,
            obj.otherDegrees,
            obj.lastName,
            obj.firstName,
            obj.middleName,
            obj.article,
            obj.title,
            obj.nickName,
            obj.streetAddress1,
            obj.streetAddress2,
            obj.streetAddress3,
            obj.city,
            obj.state,
            obj.zipCode,
            obj.country,
            obj.email1,
            obj.email2,
            obj.phone,
            obj.profession,
            obj.board,
            obj.positionHeld,
            obj.linkedIn,
            obj.facebook,
            obj.website,
            obj.publishedWork,
            obj.formCategory,
            obj.tier,
            obj.notes
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response
export_xls.short_description = u"Export as Excel spreadsheet"

class DonationFilter(SimpleListFilter):
    title = 'Donations' # or use _('country') for translated title
    parameter_name = 'donated'

    def lookups(self, request, model_admin):
        return (
            ('DONATED', 'Has donated'),
            ('NOT_DONATED', 'Hasn\'t donated')
        )

    def queryset(self, request, queryset):
        if self.value() == 'DONATED':
            return queryset.filter(donated__gt=0)
        elif self.value() == 'NOT_DONATED':
            return queryset.filter(donated__isnull=True)
        else:
            return queryset

class ContactAdmin(admin.ModelAdmin):
	def queryset(self, request):
		return Contact.objects.annotate(donated=Sum('interaction__donationAmount'))

	def total_donated(self, inst):
		return inst.donated
	total_donated.admin_order_field = 'donated' # allows you to sort by this field

	list_display = ('firstName', 'lastName', 'total_donated', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'full_address', 'city',
					'state', 'zipCode', 'email1', 'dateAdded')
	list_filter = [DonationFilter, 'state', 'graduationYear', 'board', 'positionHeld', 'tier', 'article', 'followed', 'formCategory']
	search_fields = ['firstName', 'middleName', 'lastName', 'nickName']
	inlines = [InteractionInline]
	actions = [export_xls]

class InteractionAdmin(admin.ModelAdmin):
	list_filter = ['category']

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Interaction, InteractionAdmin)
