# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('middleName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('article', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nickName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('streetAddress1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('streetAddress2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('streetAddress3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zipCode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('linkedIn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('followed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('graduationYear', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('otherDegrees', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('board', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('positionHeld', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('publishedWork', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('donationBracket', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('tier', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('formCategory', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dateAdded', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding unique constraint on 'Contact', fields ['firstName', 'lastName']
        db.create_unique(u'contacts_contact', ['firstName', 'lastName'])

        # Adding model 'Interaction'
        db.create_table(u'contacts_interaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('donationAmount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Interaction'])


    def backwards(self, orm):
        # Removing unique constraint on 'Contact', fields ['firstName', 'lastName']
        db.delete_unique(u'contacts_contact', ['firstName', 'lastName'])

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Deleting model 'Interaction'
        db.delete_table(u'contacts_interaction')


    models = {
        u'contacts.contact': {
            'Meta': {'ordering': "('firstName', 'lastName')", 'unique_together': "(['firstName', 'lastName'],)", 'object_name': 'Contact'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'board': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'donationBracket': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'followed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formCategory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'graduationYear': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'linkedIn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nickName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'otherDegrees': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'positionHeld': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publishedWork': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'streetAddress3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'contacts.interaction': {
            'Meta': {'object_name': 'Interaction'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'donationAmount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['contacts']