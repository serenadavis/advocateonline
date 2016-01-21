# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding model 'Author'
        db.create_table(u'blog_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Author'])

        # Adding model 'Images'
        db.create_table(u'blog_images', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(max_length=10000, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Images'])

        # Adding model 'Theme'
        db.create_table(u'blog_theme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Theme'])

        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('body', self.gf('redactor.fields.RedactorField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('theme', self.gf('select2.fields.ForeignKey')(to=orm['blog.Theme'], search_field=None)),
            ('first_image', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['blog.Images'], null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding M2M table for field tags on 'Post'
        m2m_table_name = db.shorten_name(u'blog_post_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'tag_id'])

        # Adding M2M table for field posted on 'Post'
        m2m_table_name = db.shorten_name(u'blog_post_posted')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('category', models.ForeignKey(orm[u'blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'category_id'])

        # Adding M2M table for field authors on 'Post'
        m2m_table_name = db.shorten_name(u'blog_post_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('author', models.ForeignKey(orm[u'blog.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting model 'Author'
        db.delete_table(u'blog_author')

        # Deleting model 'Images'
        db.delete_table(u'blog_images')

        # Deleting model 'Theme'
        db.delete_table(u'blog_theme')

        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table(db.shorten_name(u'blog_post_tags'))

        # Removing M2M table for field posted on 'Post'
        db.delete_table(db.shorten_name(u'blog_post_posted'))

        # Removing M2M table for field authors on 'Post'
        db.delete_table(db.shorten_name(u'blog_post_authors'))


    models = {
        u'blog.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'blog.images': {
            'Meta': {'object_name': 'Images'},
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'authors': ('select2.fields.ManyToManyField', [], {'to': u"orm['blog.Author']", 'search_field': 'None', 'symmetrical': 'False'}),
            'body': ('redactor.fields.RedactorField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_image': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['blog.Images']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('select2.fields.ManyToManyField', [], {'to': u"orm['blog.Category']", 'search_field': 'None', 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('select2.fields.ManyToManyField', [], {'to': u"orm['blog.Tag']", 'search_field': 'None', 'symmetrical': 'False'}),
            'theme': ('select2.fields.ForeignKey', [], {'to': u"orm['blog.Theme']", 'search_field': 'None'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'blog.theme': {
            'Meta': {'object_name': 'Theme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']