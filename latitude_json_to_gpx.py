from datetime import datetime
import json

from gpxpy.gpx import GPX, GPXTrack, GPXTrackSegment, GPXTrackPoint

with open('/Users/dlg/Downloads/coruus@gmail.com-takeout/Latitude/latitude.json', 'rb') as f:
    history = json.load(f)['data']['items'][::-1]

print len(history)

gpx = GPX()
gpx_track = GPXTrack()
gpx.tracks.append(gpx_track)

last_timestampMs = 0.0
for point in history:
    timestampMs = long(point['timestampMs'])
    if timestampMs - last_timestampMs > (1000 * 3600 * 3):
        gpx_segment = GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)
    last_timestampMs = timestampMs

    gpx_point = GPXTrackPoint(point['latitude'], point['longitude'],
            time=datetime.utcfromtimestamp(timestampMs / 1000.0))
    gpx_segment.points.append(gpx_point)

with open('latitude.gpx', 'wb') as f:
    f.write(gpx.to_xml())
