# BLDSify-the-County
Scripts to collect a land permit data, convert it to BLDS format, and upload to a PostGIS Database.

1. Document exact sources of permit data ([this may help](https://github.com/vta/GIS-Resources-Santa-Clara-County)).
1. Script out the scraping or downloading of the permit data
1. Process / convert into BLDS format
1. Write to disc and/or upload to a postgis database


## Background
The VTA wants to be able to actively monitor and track building and develepmonet and occupancy of buildings across the county through permit data.

Currently the VTA needs to be proactive to find out when and where construction is happening and tracking ends at the planning approval phase.  

Through better data and better tracking the VTA can be reactive of permits, and can possibly track projects all the way to building, construction, and occupancy phases.

With better information the VTA can track trends of where building is happening as well as ground-truth the travel models instead of the current holistic approach used today.
