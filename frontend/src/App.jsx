import { useState } from "react";

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  useMapEvents,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";
import L from "leaflet";

import "./App.css";

// =====================================================
// FIX LEAFLET MARKER ICON
// =====================================================

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png",

  iconUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png",

  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png",
});

// =====================================================
// MAP LOCATION PICKER
// =====================================================

function LocationPicker({ setLocation, setError }) {
  useMapEvents({
    click(e) {
      setError("");

      const latitude = Number(e.latlng.lat.toFixed(6));
      const longitude = Number(e.latlng.lng.toFixed(6));

      console.log("MAP CLICKED");
      console.log("Latitude:", latitude);
      console.log("Longitude:", longitude);

      setLocation({
        latitude,
        longitude,
      });
    },
  });

  return null;
}

// =====================================================
// MAIN APP
// =====================================================

function App() {
  const [location, setLocation] = useState({
    latitude: null,
    longitude: null,
  });

  const [page, setPage] = useState("home");

  const [loading, setLoading] = useState(false);

  const [results, setResults] = useState(null);

  const [error, setError] = useState("");

  // ===================================================
  // ANALYZE SITE
  // ===================================================

  const analyzeSite = async () => {
    console.log("====================================");
    console.log("ANALYZE SITE CLICKED");
    console.log("====================================");

    // ---------------------------------------------------
    // CHECK LOCATION
    // ---------------------------------------------------

    if (
      location.latitude === null ||
      location.longitude === null
    ) {
      setError(
        "Please select a location on the India map first."
      );

      return;
    }

    // ---------------------------------------------------
    // CONVERT TO NUMBERS
    // ---------------------------------------------------

    const latitude = Number(location.latitude);
    const longitude = Number(location.longitude);

    // ---------------------------------------------------
    // CHECK NUMBERS
    // ---------------------------------------------------

    if (
      !Number.isFinite(latitude) ||
      !Number.isFinite(longitude)
    ) {
      setError(
        "Invalid latitude or longitude."
      );

      return;
    }

    // ---------------------------------------------------
    // VALIDATE LATITUDE
    // ---------------------------------------------------

    if (
      latitude < -90 ||
      latitude > 90
    ) {
      setError(
        "Invalid latitude."
      );

      return;
    }

    // ---------------------------------------------------
    // VALIDATE LONGITUDE
    // ---------------------------------------------------

    if (
      longitude < -180 ||
      longitude > 180
    ) {
      setError(
        "Invalid longitude."
      );

      return;
    }

    setError("");
    setLoading(true);

    // ---------------------------------------------------
    // THIS IS THE IMPORTANT PART
    // ---------------------------------------------------
    //
    // Your Swagger screenshot shows that /analysis/
    // currently accepts ONLY:
    //
    // latitude
    // longitude
    //
    // Therefore we send ONLY those two values.
    //
    // ---------------------------------------------------

    const requestBody = {
      latitude: latitude,
      longitude: longitude,
    };

    console.log("====================================");
    console.log("SENDING TO BACKEND");
    console.log("====================================");

    console.log(
      "Latitude:",
      requestBody.latitude
    );

    console.log(
      "Longitude:",
      requestBody.longitude
    );

    console.log(
      "Request Body:",
      JSON.stringify(requestBody)
    );

    try {
      // -------------------------------------------------
      // CALL FASTAPI
      // -------------------------------------------------

      const response = await fetch(
        "http://127.0.0.1:8000/analysis/",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },

          body: JSON.stringify(requestBody),
        }
      );

      // -------------------------------------------------
      // GET RESPONSE TEXT
      // -------------------------------------------------

      const responseText =
        await response.text();

      console.log("====================================");
      console.log("BACKEND RESPONSE");
      console.log("====================================");

      console.log(
        "Status:",
        response.status
      );

      console.log(
        "Response:",
        responseText
      );

      // -------------------------------------------------
      // CONVERT RESPONSE TO JSON
      // -------------------------------------------------

      let data = {};

      if (responseText) {
        try {
          data = JSON.parse(responseText);
        } catch (jsonError) {
          console.error(
            "Response is not valid JSON:",
            jsonError
          );

          data = {
            detail: responseText,
          };
        }
      }

      // -------------------------------------------------
      // HANDLE BACKEND ERROR
      // -------------------------------------------------

      if (!response.ok) {
        let message =
          `Backend returned HTTP ${response.status}`;

        if (
          Array.isArray(data.detail)
        ) {
          message = data.detail
            .map((item) => {
              const field =
                Array.isArray(item.loc)
                  ? item.loc.join(" → ")
                  : "";

              return `${field}: ${
                item.msg ||
                "Validation error"
              }`;
            })
            .join("\n");
        } else if (
          typeof data.detail === "string"
        ) {
          message = data.detail;
        } else if (data.detail) {
          message = JSON.stringify(
            data.detail
          );
        }

        throw new Error(message);
      }

      // -------------------------------------------------
      // SUCCESS
      // -------------------------------------------------

      console.log("====================================");
      console.log("ANALYSIS SUCCESSFUL");
      console.log("====================================");

      console.log(data);

      setResults(data);

      setPage("results");
    } catch (err) {
      console.error(
        "===================================="
      );

      console.error(
        "ANALYSIS ERROR"
      );

      console.error(err);

      console.error(
        "===================================="
      );

      if (
        err.message &&
        err.message.includes(
          "Failed to fetch"
        )
      ) {
        setError(
          "Cannot connect to the backend. Make sure FastAPI is running at http://127.0.0.1:8000"
        );
      } else {
        setError(
          err.message ||
            "Analysis failed. Please check the FastAPI terminal."
        );
      }
    } finally {
      setLoading(false);
    }
  };

  // ===================================================
  // HOME PAGE
  // ===================================================

  if (page === "home") {
    return (
      <div className="app">

        {/* ============================================
            NAVBAR
        ============================================ */}

        <nav className="navbar">

          <div className="logo">

            <div className="logo-icon">
              ☀
            </div>

            <div>
              <h2>
                SolarWind AI
              </h2>

              <span>
                Renewable Energy Intelligence
              </span>
            </div>

          </div>

          <div className="nav-links">

            <button className="active">
              Home
            </button>

            <button
              onClick={() => {

                if (results) {
                  setPage("results");
                } else {
                  setError(
                    "Please analyze a site first."
                  );
                }

              }}
            >
              Site Analysis
            </button>

            <button
              onClick={() => {
                alert(
                  "SolarWind AI - Renewable Energy Site Analysis"
                );
              }}
            >
              About
            </button>

          </div>

        </nav>

        {/* ============================================
            HERO
        ============================================ */}

        <section className="hero">

          <div className="hero-content">

            <span className="hero-badge">
              AI POWERED RENEWABLE ENERGY
            </span>

            <h1>
              Find the Best Location for
              <span>
                {" "}
                Solar & Wind Deployment
              </span>
            </h1>

            <p>
              Select a location anywhere in India
              to analyze its renewable energy
              potential, site suitability, energy
              yield and deployment feasibility.
            </p>

          </div>

        </section>

        {/* ============================================
            MAP / ANALYSIS SECTION
        ============================================ */}

        <section className="analysis-section">

          <div className="section-heading">

            <div>

              <span className="section-label">
                STEP 01
              </span>

              <h2>
                Select Your Site
              </h2>

              <p>
                Click anywhere on the map to select
                a location in India.
              </p>

            </div>

          </div>

          <div className="analysis-layout">

            {/* ========================================
                MAP
            ======================================== */}

            <div className="map-card">

              <MapContainer
                center={[
                  22.5937,
                  78.9629,
                ]}
                zoom={5}
                minZoom={4}
                maxZoom={12}
                scrollWheelZoom={true}
                className="india-map"
              >

                <TileLayer
                  attribution="&copy; OpenStreetMap contributors"
                  url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />

                <LocationPicker
                  setLocation={setLocation}
                  setError={setError}
                />

                {location.latitude !== null &&
                  location.longitude !== null && (

                    <Marker
                      position={[
                        location.latitude,
                        location.longitude,
                      ]}
                    >

                      <Popup>

                        <strong>
                          Selected Site
                        </strong>

                        <br />

                        Latitude:{" "}
                        {location.latitude}

                        <br />

                        Longitude:{" "}
                        {location.longitude}

                      </Popup>

                    </Marker>

                  )}

              </MapContainer>

            </div>

            {/* ========================================
                LOCATION CARD
            ======================================== */}

            <div className="location-card">

              <div className="location-header">

                <div className="location-icon">
                  📍
                </div>

                <div>

                  <h3>
                    Selected Location
                  </h3>

                  <p>
                    Select a point on the map
                  </p>

                </div>

              </div>

              {/* ====================================
                  COORDINATES
              ==================================== */}

              <div className="coordinates">

                {/* LATITUDE */}

                <div className="coordinate-box">

                  <label>
                    LATITUDE
                  </label>

                  <input
                    type="text"
                    value={
                      location.latitude === null
                        ? ""
                        : location.latitude
                    }
                    placeholder="Select from map"
                    readOnly
                  />

                  <span>
                    ° N / S
                  </span>

                </div>

                {/* LONGITUDE */}

                <div className="coordinate-box">

                  <label>
                    LONGITUDE
                  </label>

                  <input
                    type="text"
                    value={
                      location.longitude === null
                        ? ""
                        : location.longitude
                    }
                    placeholder="Select from map"
                    readOnly
                  />

                  <span>
                    ° E / W
                  </span>

                </div>

              </div>

              {/* ====================================
                  ERROR
              ==================================== */}

              {error && (

                <div className="error-message">
                  {error}
                </div>

              )}

              {/* ====================================
                  ANALYZE BUTTON
              ==================================== */}

              <button
                className="analyze-button"
                onClick={analyzeSite}
                disabled={
                  loading ||
                  location.latitude === null ||
                  location.longitude === null
                }
              >

                {loading ? (
                  <>
                    <span className="spinner"></span>

                    Analyzing Site...
                  </>
                ) : (
                  <>
                    Analyze Site

                    <span>
                      →
                    </span>
                  </>
                )}

              </button>

              {/* ====================================
                  TIP
              ==================================== */}

              <div className="map-tip">

                <span>
                  💡
                </span>

                <p>
                  Click anywhere on the map to
                  automatically capture latitude
                  and longitude.
                </p>

              </div>

            </div>

          </div>

        </section>

        {/* ============================================
            FEATURES
        ============================================ */}

        <section className="features-section">

          <div className="feature">

            <div className="feature-icon solar">
              ☀
            </div>

            <h3>
              Solar Potential
            </h3>

            <p>
              Analyze solar irradiance and
              expected solar energy generation.
            </p>

          </div>

          <div className="feature">

            <div className="feature-icon wind">
              ♨
            </div>

            <h3>
              Wind Potential
            </h3>

            <p>
              Evaluate wind speed, wind class
              and wind energy potential.
            </p>

          </div>

          <div className="feature">

            <div className="feature-icon site">
              ✓
            </div>

            <h3>
              Site Suitability
            </h3>

            <p>
              Evaluate terrain, infrastructure
              and environmental conditions.
            </p>

          </div>

          <div className="feature">

            <div className="feature-icon energy">
              ⚡
            </div>

            <h3>
              Energy Yield
            </h3>

            <p>
              Estimate annual renewable energy
              generation for the site.
            </p>

          </div>

        </section>

        {/* ============================================
            FOOTER
        ============================================ */}

        <footer>

          <div>

            <strong>
              SolarWind AI
            </strong>

            <span>
              {" "}
              • Intelligent Renewable Energy
              Planning
            </span>

          </div>

          <span>
            © 2026 SolarWind AI
          </span>

        </footer>

      </div>
    );
  }

  // ===================================================
  // RESULTS PAGE
  // ===================================================

  return (
    <div className="app">

      {/* ============================================
          NAVBAR
      ============================================ */}

      <nav className="navbar">

        <div className="logo">

          <div className="logo-icon">
            ☀
          </div>

          <div>

            <h2>
              SolarWind AI
            </h2>

            <span>
              Renewable Energy Intelligence
            </span>

          </div>

        </div>

        <button
          className="back-button"
          onClick={() => setPage("home")}
        >
          ← Back to Map
        </button>

      </nav>

      {/* ============================================
          RESULTS
      ============================================ */}

      <main className="results-page">

        <div className="results-header">

          <span className="hero-badge">
            SITE ANALYSIS COMPLETE
          </span>

          <h1>
            Renewable Energy Site Results
          </h1>

          <p>
            Analysis results for the selected
            location.
          </p>

        </div>

        {/* ========================================
            SELECTED LOCATION
        ======================================== */}

        <div className="selected-location">

          <div>

            <span>
              SELECTED LOCATION
            </span>

            <h3>
              📍 {location.latitude},{" "}
              {location.longitude}
            </h3>

          </div>

          <div className="status">
            ✓ Analysis Complete
          </div>

        </div>

        {/* ========================================
            RESULT GRID
        ======================================== */}

        <div className="result-grid">

          {/* SOLAR */}

          <div className="result-card">

            <div className="result-icon solar">
              ☀
            </div>

            <div>

              <span>
                Solar Potential
              </span>

              <h2>
                {getNestedValue(
                  results,
                  [
                    "solar_assessment",
                    "solar_irradiance",
                  ]
                )}
              </h2>

              <small>
                Solar Irradiance
              </small>

            </div>

          </div>

          {/* WIND */}

          <div className="result-card">

            <div className="result-icon wind">
              ♨
            </div>

            <div>

              <span>
                Wind Potential
              </span>

              <h2>
                {getNestedValue(
                  results,
                  [
                    "wind_assessment",
                    "wind_speed",
                  ]
                )}
              </h2>

              <small>
                Wind Speed
              </small>

            </div>

          </div>

          {/* SITE */}

          <div className="result-card">

            <div className="result-icon site">
              ✓
            </div>

            <div>

              <span>
                Site Suitability
              </span>

              <h2>
                {getNestedValue(
                  results,
                  [
                    "technical_feasibility",
                    "score",
                  ]
                )}
              </h2>

              <small>
                Technical Feasibility Score
              </small>

            </div>

          </div>

          {/* ENERGY */}

          <div className="result-card">

            <div className="result-icon energy">
              ⚡
            </div>

            <div>

              <span>
                Annual Energy
              </span>

              <h2>
                {getNestedValue(
                  results,
                  [
                    "energy_yield",
                    "total_estimated_annual_energy",
                  ]
                )}
              </h2>

              <small>
                Estimated Annual Energy
              </small>

            </div>

          </div>

        </div>

        {/* ========================================
            ENVIRONMENTAL DATA
        ======================================== */}

        <section className="details-card">

          <div className="details-header">

            <div>

              <span className="section-label">
                ENVIRONMENTAL DATA
              </span>

              <h2>
                Site Information
              </h2>

            </div>

          </div>

          <div className="details-grid">

            <Detail
              label="Latitude"
              value={`${location.latitude}°`}
            />

            <Detail
              label="Longitude"
              value={`${location.longitude}°`}
            />

            <Detail
              label="Solar Irradiance"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "solar_irradiance",
                ]
              )}
            />

            <Detail
              label="Temperature"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "temperature",
                ]
              )}
            />

            <Detail
              label="Humidity"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "relative_humidity",
                ]
              )}
            />

            <Detail
              label="Elevation"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "elevation",
                ]
              )}
            />

            <Detail
              label="Slope"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "slope",
                ]
              )}
            />

            <Detail
              label="Wind Speed"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "wind_speed",
                ]
              )}
            />

            <Detail
              label="Power Density"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "power_density",
                ]
              )}
            />

            <Detail
              label="Distance to Road"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "distance_to_road",
                ]
              )}
            />

            <Detail
              label="Total Roads"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "total_roads",
                ]
              )}
            />

            <Detail
              label="Accessibility"
              value={getNestedValue(
                results,
                [
                  "environmental_data",
                  "accessibility",
                ]
              )}
            />

          </div>

        </section>

        {/* ========================================
            DEPLOYMENT ASSESSMENT
        ======================================== */}

        <section className="details-card">

          <div className="details-header">

            <div>

              <span className="section-label">
                DEPLOYMENT ASSESSMENT
              </span>

              <h2>
                Recommended Deployment
              </h2>

            </div>

          </div>

          <div className="details-grid">

            <Detail
              label="Technical Feasibility"
              value={getNestedValue(
                results,
                [
                  "technical_feasibility",
                  "status",
                ]
              )}
            />

            <Detail
              label="Feasibility Score"
              value={getNestedValue(
                results,
                [
                  "technical_feasibility",
                  "score",
                ]
              )}
            />

            <Detail
              label="Wind Class"
              value={getNestedValue(
                results,
                [
                  "wind_assessment",
                  "wind_class",
                ]
              )}
            />

            <Detail
              label="Capacity Factor"
              value={getNestedValue(
                results,
                [
                  "wind_assessment",
                  "capacity_factor",
                ]
              )}
            />

            <Detail
              label="Recommended Technology"
              value={getNestedValue(
                results,
                [
                  "recommended_deployment",
                  "recommended_technology",
                ]
              )}
            />

            <Detail
              label="Recommended Capacity"
              value={getNestedValue(
                results,
                [
                  "recommended_deployment",
                  "recommended_capacity",
                ]
              )}
            />

          </div>

        </section>

        {/* ========================================
            FINANCIAL ANALYSIS
        ======================================== */}

        <section className="details-card">

          <div className="details-header">

            <div>

              <span className="section-label">
                FINANCIAL ANALYSIS
              </span>

              <h2>
                Project Economics
              </h2>

            </div>

          </div>

          <div className="details-grid">

            <Detail
              label="Annual Energy Yield"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "annual_energy_yield",
                ]
              )}
            />

            <Detail
              label="Electricity Tariff"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "electricity_tariff",
                ]
              )}
            />

            <Detail
              label="Annual Revenue"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "annual_revenue",
                ]
              )}
            />

            <Detail
              label="Installed Capacity"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "installed_capacity_mw",
                ]
              )}
            />

            <Detail
              label="Project Cost"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "estimated_project_cost",
                ]
              )}
            />

            <Detail
              label="Payback Period"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "payback_period",
                ]
              )}
            />

            <Detail
              label="ROI"
              value={getNestedValue(
                results,
                [
                  "financial_metrics",
                  "roi",
                ]
              )}
            />

          </div>

        </section>

        {/* ========================================
            RAW BACKEND RESPONSE
        ======================================== */}

        {results && (

          <details className="raw-results">

            <summary>
              View complete analysis response
            </summary>

            <pre>
              {JSON.stringify(
                results,
                null,
                2
              )}
            </pre>

          </details>

        )}

      </main>

    </div>
  );
}

// =====================================================
// DETAIL COMPONENT
// =====================================================

function Detail({ label, value }) {
  return (
    <div>

      <span>
        {label}
      </span>

      <strong>
        {value}
      </strong>

    </div>
  );
}

// =====================================================
// SAFE NESTED VALUE
// =====================================================

function getNestedValue(
  object,
  keys,
  fallback = "—"
) {
  if (!object) {
    return fallback;
  }

  let value = object;

  for (const key of keys) {

    if (
      value === null ||
      value === undefined ||
      value[key] === undefined ||
      value[key] === null
    ) {
      return fallback;
    }

    value = value[key];
  }

  return value;
}

// =====================================================
// DEFAULT EXPORT
// =====================================================

export default App;