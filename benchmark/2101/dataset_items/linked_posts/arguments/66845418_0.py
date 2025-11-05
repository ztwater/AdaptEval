import folium
from folium.elements import JSCSSMixin
from folium.map import Layer
from jinja2 import Template


class StyledGeoJson(JSCSSMixin, Layer):
    """
    Creates a GeoJson which supports.

    """
    _template = Template(u"""
        {% macro script(this, kwargs) %}

            var {{ this.get_name() }} = L.geoJson({{ this.data }},
                {
                    useSimpleStyle: true,
                    useMakiMarkers: true
                }
            ).addTo({{ this._parent.get_name() }});
        {% endmacro %}
        """)  

    default_js = [
        ('leaflet-simplestyle', 'https://unpkg.com/leaflet-simplestyle'),
    ]

    def __init__(self, data,name=None, overlay=True, control=True, show=True):
        super(StyledGeoJson, self).__init__(name=name, overlay=overlay,
                                       control=control, show=show)
        self._name = 'StyledGeoJson'
        self.data = data
