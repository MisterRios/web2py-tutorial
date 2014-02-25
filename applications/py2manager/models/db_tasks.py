#defines the database table # defines unique companies
db.define_table('company',
	Field('company_name', notnull=True, unique=True),
	Field('email'),
	Field('phone', notnull=True),
	Field('url'),
	format = '%(company_name)s' #what is this exactly?
	)

db.company.email.requires=IS_EMAIL() 
#set requirements for field to be email, cannot define in SQL
db.company.url.requires=IS_EMPTY_OR(IS_URL())
#same, but pass IS_URL to the IS_EMPTY_OR function. Genius.

db.define_table('project', #table name
	Field('name', notnull=True), #field definition
	Field('employee_name', db.auth_user, default=auth.user_id), #creates new db for auth_user
	Field('company_name', 'reference company', notnull=True), #pulls from above
	Field('description', 'text', notnull=True),
	Field('start_date', 'date', notnull=True), 
	Field('due_date', 'date', notnull=True),
	Field('completed', 'boolean', notnull=True),
	format = '%(company_name)s'
	)

db.project.employee_name.readable = True
db.project.employee_name.writable = False