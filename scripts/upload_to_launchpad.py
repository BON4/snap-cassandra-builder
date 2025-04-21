import launchpadlib.launchpad
import os

creds_file = os.path.expanduser("~/.cache/lp-creds")

lp = launchpadlib.launchpad.Launchpad.login_with(
    'Cassandra Uploader',
    'production',
    version='devel',
    credentials_file=creds_file
)

project = lp.projects['cassandra-releases']

with open('cassandra.tar.gz', 'rb') as f:
    project.add_attachment(f, 'cassandra-4.1.3.tar.gz', 'application/gzip')

print("✅ Tarball uploaded successfully!")
