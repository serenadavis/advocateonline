## Setting Up the Search Engine

###Setup on unix and linux

First, install the Solr Engine backend.  Navigate to the install directory, and download the tarball

```curl -LO https://archive.apache.org/dist/lucene/solr/4.10.2/solr-4.10.2.tgz ```

Now simply unpack the archive

```tar xvzf solr-4.10.2```

To start Solr navigate to 

```cd solr-4.10.2/example```

and execute

```java -jar start.jar```

As is, the Solr engine is not ready to build any indexes or execute any queries, but it should start with no errors.



Next, the haystack interface needs to be installed and used to generate a Solr Schema.  To start, navigate to the django app directory and install the haystack packages

```pip install django-haystack```

Now, ensure the django environment is up to date with the advocateonline github repo so that ```settings.py``` is configured to interface with Solr.  By default Solr will listen on 8983, but if it has been configured to listen on a custom port, ```settings.py``` will need to be configured thus.  In ```settings.py``` navigate to ```HAYSTACK_CONNECTIONS = {...``` and where it reads ```'URL': 'https://127.0.0.1:8983/solr'``` modify this to ```'URL': 'https://127.0.0.1:<new_port_number_here>/solr'```.

Now, ensure that the app also includes the most recent version of ```search_indexes.py```.  If this is the case, navigate back to the app root directory and execute 

```./manage.py build_solr_schema > schema.xml```

Now take the ```schema.xml``` file just generated and move it back to the newly created Solr directory

```mv schema.xml .../solr-4.10.2/examples/solr/collection1/conf/```

Now that the schema has been established, stop the Solr engine, navigate back to the django app directory and build the initial Solr index 

```./manage.py rebuild_index```

Say yes at any prompts, and upon completing successfully, the number of context items indexed will be displayed.  Now, simply restart the Solr engine as before 

```java -jar start.jar```

and if everything has proceeded without errors, Solr should be ready to execute queries, and the django app configured to query the Solr backend.  To access the Solr admin portal, in any web browser, simply navigate to

```localhost:8983/solr```

To update the index, either 

```./manage.py rebuild_index```

or 

```./manage.py update_index```

may be executed manually or set as cron jobs.  Note: rebuild_index is less efficient, as it will flush any existing index and rebuild the indexes from scratch every time, and depending on the number of content items to index, may take a non-trivial time to execute.

###Setup on mac