# Metadata
1. Download SQLite Database `wget http://millionsongdataset.com/sites/default/files/AdditionalFiles/track_metadata.db`
2. Ensure SQLite installed `sudo apt-get install sqlite3`
3. Run `sqlite3 -header -csv track_metadata.db "select * from songs" > songs.csv`
# Sample set
1. Download dataset `wget http://labrosa.ee.columbia.edu/~dpwe/tmp/millionsongsubset.tar.gz`
