## Setting Up the Search Engine (Linux or Mac)

First, ensure that Java is installed on the machine.  To check, execute

```
java -version
```

If this successfully returns your Java RE version, proceed to Solr Engine installation.  If not, JRE must be installed before proceeding.  On ```yum``` machine this can be accomplished with 

```yum install java-1.8.0-openjdk.i686    or    yum install java-1.8.0-openjdk.x86_64```

and with apt-get

```apt-get install default-jre```

Next, install the Solr Engine backend.  Navigate to the install directory, and download the tarball

```curl -LO https://archive.apache.org/dist/lucene/solr/4.10.2/solr-4.10.2.tgz ```

Now simply unpack the archive

```tar xvzf solr-4.10.2.tgz```

To start Solr navigate to 

```cd solr-4.10.2/example```

and execute

```java -jar start.jar```

As is, the Solr engine is not ready to build any indexes or execute any queries, but it should start with no errors.  If so, stop it for now.



Next, the haystack interface needs to be installed and used to generate a Solr Schema.  To start, ensure that the virtualenv has the most recent ```requirements.txt``` satisfied.  Also be sure that the django app includes the most recent advocateonline repo which must include, for search sake, ```search_settings.py```, ```search_indexes.py```, ```templates/search/...*``` to name the most vital.

NOTE: By default Solr will listen on 8983, but if it has been configured to listen on a custom port, ```search_settings.py``` will need to be updated accordingly.  In this case, within ```search_settings.py``` navigate to ```HAYSTACK_CONNECTIONS = {...``` and where it reads ```'URL': 'https://127.0.0.1:8983/solr'``` modify this to ```'URL': 'https://127.0.0.1:<new_port_number_here>/solr'```.

Now, if the app is up to date and all requirements are met, navigate back to the app root directory and execute 

```./manage.py build_solr_schema > schema.xml```

Now take the ```schema.xml``` file just generated and move it back to the newly created Solr directory

```mv schema.xml .../solr-4.10.2/example/solr/collection1/conf/```

Now that the schema has been established, restart the Solr engine as before by navigating to 

``` solr-4.10-2/example ```

and executing 

```java -jar start.jar```

If Solr starts with no errors, navigate back to the django app directory and build the initial Solr index 

```./manage.py rebuild_index```

Say yes at any prompts, and upon completing successfully, the number of context items indexed will be displayed.  If everything has proceeded without errors, Solr should be ready to execute queries, and the django app configured to query the Solr backend.  To access the Solr admin portal, in any web browser, simply navigate to

``` localhost:8983/solr ```

To update the index, either 

```./manage.py rebuild_index```

or 

```./manage.py update_index```

may be executed manually or set as cron jobs.  

IMPORTANT EFFICIENCY NOTE: rebuild_index is less efficient, as it will flush any existing index and rebuild the indexes from scratch every time, and depending on the number of content items to index, may take a non-trivial time to execute.
