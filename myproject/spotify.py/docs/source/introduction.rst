============
Introduction
============

Getting Started
###############

API Coverage
************

Currently the library offers full http api coverage, this includes the regular
REST API and the Connect Web API (used for maniplulating playback smoothly.)

If there is missing coverage of a Spotify API feature feel free to open a 
Github Issue and we can sort out the implementation from there.

Concepts
********

Abstractions!
~~~~~~~~~~~~~

The library is abstracted into mainly three components:

 - The very low level (``spotify.http``)
 - The very high level (``spotify.models``, ``spotify.oauth`` and ``spotify.utils``)
 - The synchronous interface (``spotify.sync``)

``spotify.http``
~~~~~~~~~~~~~~~~

The HTTP submodule is ultimately comprised of two main components:

 - ``spotify.http.HTTPClient``
 - ``spotify.http.HTTPUserClient``
 
``spotify.models``
~~~~~~~~~~~~~~~~~~

All the models are located under ``spotify.models``.

 - ``spotify.SpotifyBase``
 - ``spotify.URIBase``
 - ``spotify.Device``
 - ``spotify.Context``
 - ``spotify.Image``
 - ``spotify.Artist``
 - ``spotify.Track``
 - ``spotify.PlaylistTrack``
 - ``spotify.Player``
 - ``spotify.Album``
 - ``spotify.Library``
 - ``spotify.Playlist``
 - ``spotify.User``

``spotify.oauth``
~~~~~~~~~~~~~~~~~

The oauth module concerns itself will all OAuth2 related logic.

 - ``spotify.OAuth2``
 - ``spotify.get_required_scopes``

``spotify.utils``
~~~~~~~~~~~~~~~~~

The utils module aims to provide usefull helpers.

 - ``spotify.to_id``

``spotify.sync``
~~~~~~~~~~~~~~~~~

The sync module aims to provide a one to one interface with the regular module.
Whilst hiding any `async/await` shennanigans so that users don't need to be
restricted by their executing environment.

Guidelines
**********

Writing a Query
~~~~~~~~~~~~~~~

Queries are mainly done through :meth:`spotify.Client.search`.

Keyword matching
----------------

Matching of search keywords is not case-sensitive. Operators, however, should
be specified in uppercase. Unless surrounded by double quotation marks,
keywords are matched in any order.

For example:

 - ``q="roadhouse blues"`` matches both ``“Blues Roadhouse”`` and ``“Roadhouse of the Blues”``.
 - ``q="\"roadhouse blues\""`` matches ``“My Roadhouse Blues”`` but not ``“Roadhouse of the Blues”.``

Searching
---------

Searching for playlists returns results where the query keyword(s) match any
part of the playlist’s name or description. Only popular public playlists are
returned.

Operators
---------

.. note::

    Operators must be specified in uppercase. Otherwise, they are handled as normal keywords to be matched.

The operator ``NOT`` can be used to exclude results.

For example: ``q="roadhouse NOT blues"`` returns items that match
``“roadhouse”`` but excludes those that also contain the keyword ``“blues”``.

Similarly, the ``OR`` operator can be used to broaden the search:
``q="roadhouse OR blues"`` returns all the results that include either of the
terms.

.. warning::

    Only one ``OR`` operator can be used in a query.

Wildcards
---------

The asterisk (``*``) character can, with some limitations, be used as a
wildcard (maximum: 2 per query). It matches a variable number of
non-white-space characters.

It cannot be used:

 - in a quoted phrase
 - in a field filter
 - when there is a dash (``-``) in the query
 - or as the first character of the keyword string Field filters: By default,
   results are returned when a match is found in any field of the target
   object type. Searches can be made more specific by specifying an album,
   artist or track field filter.

For example: The query ``q="album:gold artist:abba", types=["album"]`` returns
only albums with the text ``“gold”`` in the album name and the text ``“abba”``
in the artist name.

To limit the results to a particular year, use the field filter year with
album, artist, and track searches.

For example: ``q="bob year:2014"``

Or with a date range. For example: ``q="bob year:1980-2020"``

To retrieve only albums released in the last two weeks, use the field filter
``tag:new`` in album searches.

To retrieve only albums with the lowest 10% popularity, use the field filter
``tag:hipster`` in album searches.

.. note::

    This field filter only works with album searches.

Depending on object types being searched for, other field filters, include
genre (applicable to tracks and artists), upc, and isrc. For example:
``q="lil genre:\"southern hip hop\", types=["artist"]``. Use double quotation
marks around the genre keyword string if it contains spaces.
