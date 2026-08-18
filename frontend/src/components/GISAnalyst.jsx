import "./GISAnalyst.scss";

function GISAnalyst({ data }) {
  if (!data) {
    return null;
  }

  const environmental =
    data.environmental_data || {};

  const location =
    data.location || {};

  return (
    <section className="gis-analyst">

      <div className="gis-header">
        <div>
          <span className="gis-label">
            GIS ANALYST
          </span>

          <h2>
            Geographic Site Analysis
          </h2>

          <p>
            Location-based environmental and
            infrastructure information.
          </p>
        </div>

        <div className="gis-location">
          📍 {location.latitude ?? "—"},{" "}
          {location.longitude ?? "—"}
        </div>
      </div>

      <div className="gis-grid">

        <div className="gis-card">
          <span>Elevation</span>

          <strong>
            {environmental.elevation ?? "—"}
          </strong>

          <small>
            meters
          </small>
        </div>

        <div className="gis-card">
          <span>Solar Irradiance</span>

          <strong>
            {environmental.solar_irradiance ?? "—"}
          </strong>

          <small>
            site value
          </small>
        </div>

        <div className="gis-card">
          <span>Wind Speed</span>

          <strong>
            {environmental.wind_speed ?? "—"}
          </strong>

          <small>
            site value
          </small>
        </div>

        <div className="gis-card">
          <span>Power Density</span>

          <strong>
            {environmental.power_density ?? "—"}
          </strong>

          <small>
            site value
          </small>
        </div>

        <div className="gis-card">
          <span>Distance to Road</span>

          <strong>
            {environmental.distance_to_road ?? "—"}
          </strong>

          <small>
            km
          </small>
        </div>

        <div className="gis-card">
          <span>Total Roads</span>

          <strong>
            {environmental.total_roads ?? "—"}
          </strong>

          <small>
            detected roads
          </small>
        </div>

        <div className="gis-card">
          <span>Accessibility</span>

          <strong>
            {environmental.accessibility ?? "—"}
          </strong>

          <small>
            OSM analysis
          </small>
        </div>

        <div className="gis-card">
          <span>Road Types</span>

          <strong>
            {environmental.unique_road_types ?? "—"}
          </strong>

          <small>
            unique types
          </small>
        </div>

      </div>

    </section>
  );
}

export default GISAnalyst;