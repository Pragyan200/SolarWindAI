import "./style.css";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const app = document.getElementById("app");

app.innerHTML = `
<header class="navbar">
  <div class="brand">
    <div class="brand-icon">☀️</div>
    <div>
      <div class="brand-name">SolarWind AI</div>
      <div class="brand-subtitle">RENEWABLE ENERGY INTELLIGENCE</div>
    </div>
  </div>

  <nav>
    <a href="#home">Home</a>
    <a href="#analysis">Site Analysis</a>
    <a href="#about">About</a>
  </nav>
</header>

<main id="home">

  <section class="hero">
    <div class="hero-content">

      <div class="badge">
        AI POWERED RENEWABLE ENERGY PLATFORM
      </div>

      <h1>
        Intelligent Solar & Wind
        <span>Site Deployment</span>
      </h1>

      <p>
        Discover suitable locations for solar and wind
        energy deployment across India using AI-powered
        site analysis and energy estimation.
      </p>

      <a href="#analysis" class="hero-button">
        Start Site Analysis →
      </a>

    </div>
  </section>


  <section id="analysis" class="analysis-section">

    <div class="section-title">
      <div class="step">STEP 01</div>

      <h2>Select Your Deployment Site</h2>

      <p>
        Click anywhere on the India map to select your location.
      </p>
    </div>


    <div class="analysis-container">

      <div class="map-wrapper">

        <div class="map-top">

          <div>
            <strong>India Renewable Energy Map</strong>
            <span>Click on the map to select a site</span>
          </div>

          <div class="map-status">
            ● LIVE MAP
          </div>

        </div>

        <div id="map"></div>

      </div>


      <aside class="location-panel">

        <div class="panel-icon">📍</div>

        <h3>Selected Location</h3>

        <p class="panel-description">
          Select a point on the map to automatically
          obtain latitude and longitude.
        </p>


        <div class="coordinate-group">

          <label>LATITUDE</label>

          <div class="coordinate-input">

            <input
              id="latitude"
              type="text"
              placeholder="Select location"
              readonly
            />

            <span>°</span>

          </div>

        </div>


        <div class="coordinate-group">

          <label>LONGITUDE</label>

          <div class="coordinate-input">

            <input
              id="longitude"
              type="text"
              placeholder="Select location"
              readonly
            />

            <span>°</span>

          </div>

        </div>


        <div
          id="location-message"
          class="location-message"
        >
          📌 Click on the map to select your site.
        </div>


        <button
          id="analyze-button"
          class="analyze-button"
        >
          Analyze Site →
        </button>


        <div class="tip">

          <strong>💡 How it works</strong>

          <p>
            Select a location on the map.
            SolarWind AI will analyze the selected
            site using the renewable energy analysis engine.
          </p>

        </div>

      </aside>

    </div>

  </section>


  <section class="features" id="about">

    <div class="section-title center">

      <div class="step">
        PLATFORM CAPABILITIES
      </div>

      <h2>
        Complete Renewable Energy Analysis
      </h2>

    </div>


    <div class="feature-grid">

      <div class="feature-card">

        <div class="feature-icon solar">
          ☀️
        </div>

        <h3>Solar Potential</h3>

        <p>
          Analyze solar irradiance and expected
          solar energy generation.
        </p>

      </div>


      <div class="feature-card">

        <div class="feature-icon wind">
          💨
        </div>

        <h3>Wind Potential</h3>

        <p>
          Evaluate wind speed, wind classification
          and wind energy potential.
        </p>

      </div>


      <div class="feature-card">

        <div class="feature-icon suitability">
          ✓
        </div>

        <h3>Site Suitability</h3>

        <p>
          Evaluate terrain, infrastructure,
          environmental and economic conditions.
        </p>

      </div>


      <div class="feature-card">

        <div class="feature-icon energy">
          ⚡
        </div>

        <h3>Energy Estimation</h3>

        <p>
          Estimate annual renewable energy
          generation using the prediction model.
        </p>

      </div>

    </div>

  </section>

</main>


<section
  id="results-page"
  class="results-page hidden"
>

  <div class="results-header">

    <button
      id="back-button"
      class="back-button"
    >
      ← Back to Map
    </button>

    <div class="badge">
      SITE ANALYSIS COMPLETE
    </div>

    <h1>
      Renewable Energy
      <span>Site Results</span>
    </h1>

    <p>
      AI-powered analysis of your selected location.
    </p>

  </div>


  <div class="selected-location-card">

    <div>

      <small>
        SELECTED LOCATION
      </small>

      <h3 id="result-location">
        —
      </h3>

    </div>

    <div class="complete">
      ✓ Analysis Complete
    </div>

  </div>


  <div class="result-grid">

    <div class="result-card">

      <div class="result-symbol solar">
        ☀️
      </div>

      <div>

        <small>
          SOLAR POTENTIAL
        </small>

        <h2 id="solar-result">
          —
        </h2>

        <p>
          Solar Irradiance
        </p>

      </div>

    </div>


    <div class="result-card">

      <div class="result-symbol wind">
        💨
      </div>

      <div>

        <small>
          WIND POTENTIAL
        </small>

        <h2 id="wind-result">
          —
        </h2>

        <p>
          Wind Speed
        </p>

      </div>

    </div>


    <div class="result-card">

      <div class="result-symbol suitability">
        ✓
      </div>

      <div>

        <small>
          SITE SUITABILITY
        </small>

        <h2 id="score-result">
          —
        </h2>

        <p>
          Overall Site Score
        </p>

      </div>

    </div>


    <div class="result-card">

      <div class="result-symbol energy">
        ⚡
      </div>

      <div>

        <small>
          ANNUAL ENERGY
        </small>

        <h2 id="energy-result">
          —
        </h2>

        <p>
          Estimated Energy Yield
        </p>

      </div>

    </div>

  </div>


  <!-- =====================================================
       BASIC SITE ASSESSMENT
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        SITE ASSESSMENT
      </div>

      <h2>
        Deployment Analysis
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Latitude</small>
        <strong id="detail-latitude">—</strong>
      </div>


      <div class="detail">
        <small>Longitude</small>
        <strong id="detail-longitude">—</strong>
      </div>


      <div class="detail">
        <small>Wind Class</small>
        <strong id="detail-wind-class">—</strong>
      </div>


      <div class="detail">
        <small>Capacity Factor</small>
        <strong id="detail-capacity-factor">—</strong>
      </div>


      <div class="detail">
        <small>Energy Prediction</small>
        <strong id="detail-prediction">—</strong>
      </div>


      <div class="detail">
        <small>Deployment Strategy</small>
        <strong id="detail-deployment">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       ENVIRONMENTAL DATA
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        ENVIRONMENTAL DATA
      </div>

      <h2>
        Site & Meteorological Potential
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Solar Irradiance</small>
        <strong id="detail-solar-irradiance">—</strong>
      </div>


      <div class="detail">
        <small>Temperature</small>
        <strong id="detail-temperature">—</strong>
      </div>


      <div class="detail">
        <small>Relative Humidity</small>
        <strong id="detail-humidity">—</strong>
      </div>


      <div class="detail">
        <small>Elevation</small>
        <strong id="detail-elevation">—</strong>
      </div>


      <div class="detail">
        <small>Slope</small>
        <strong id="detail-slope">—</strong>
      </div>


      <div class="detail">
        <small>Wind Speed</small>
        <strong id="detail-wind-speed">—</strong>
      </div>


      <div class="detail">
        <small>Power Density</small>
        <strong id="detail-power-density">—</strong>
      </div>


      <div class="detail">
        <small>Total Roads</small>
        <strong id="detail-total-roads">—</strong>
      </div>


      <div class="detail">
        <small>Unique Road Types</small>
        <strong id="detail-road-types">—</strong>
      </div>


      <div class="detail">
        <small>Distance to Road</small>
        <strong id="detail-distance-road">—</strong>
      </div>


      <div class="detail">
        <small>Distance to Grid</small>
        <strong id="detail-distance-grid">—</strong>
      </div>


      <div class="detail">
        <small>Accessibility</small>
        <strong id="detail-accessibility">—</strong>
      </div>


      <div class="detail">
        <small>Land Area</small>
        <strong id="detail-land-area">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       SITE SUITABILITY
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        SITE SUITABILITY
      </div>

      <h2>
        Suitability Score Breakdown
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Renewable Resource Score</small>
        <strong id="detail-renewable-score">—</strong>
      </div>


      <div class="detail">
        <small>Terrain Score</small>
        <strong id="detail-terrain-score">—</strong>
      </div>


      <div class="detail">
        <small>Infrastructure Score</small>
        <strong id="detail-infrastructure-score">—</strong>
      </div>


      <div class="detail">
        <small>Environmental Score</small>
        <strong id="detail-environmental-score">—</strong>
      </div>


      <div class="detail">
        <small>Economic Score</small>
        <strong id="detail-economic-score">—</strong>
      </div>


      <div class="detail">
        <small>Overall Suitability</small>
        <strong id="detail-overall-score">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       TECHNICAL FEASIBILITY
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        TECHNICAL FEASIBILITY
      </div>

      <h2>
        Feasibility & Constraint Analysis
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Status</small>
        <strong id="detail-feasibility-status">—</strong>
      </div>


      <div class="detail">
        <small>Feasibility Score</small>
        <strong id="detail-feasibility-score">—</strong>
      </div>


      <div class="detail">
        <small>Grid Distance</small>
        <strong id="detail-feasibility-grid">—</strong>
      </div>


      <div class="detail">
        <small>Road Distance</small>
        <strong id="detail-feasibility-road">—</strong>
      </div>


      <div class="detail">
        <small>Accessibility</small>
        <strong id="detail-feasibility-accessibility">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       ML PREDICTION
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        AI PREDICTION
      </div>

      <h2>
        ML Prediction & Driver Explanation
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Predicted Energy</small>
        <strong id="detail-ml-energy">—</strong>
      </div>


      <div class="detail">
        <small>Primary Driver</small>
        <strong id="detail-primary-driver">—</strong>
      </div>


      <div class="detail">
        <small>Secondary Driver</small>
        <strong id="detail-secondary-driver">—</strong>
      </div>


      <div class="detail">
        <small>Prediction Message</small>
        <strong id="detail-ml-message">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       DEPLOYMENT RECOMMENDATION
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        DEPLOYMENT RECOMMENDATION
      </div>

      <h2>
        Recommended Renewable Deployment
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Technology</small>
        <strong id="detail-recommended-technology">—</strong>
      </div>


      <div class="detail">
        <small>Recommended Capacity</small>
        <strong id="detail-recommended-capacity">—</strong>
      </div>


      <div class="detail">
        <small>Expansion Status</small>
        <strong id="detail-expansion-status">—</strong>
      </div>


      <div class="detail">
        <small>Optimization Remarks</small>
        <strong id="detail-optimization-remarks">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       ENERGY YIELD
  ====================================================== -->

  <div class="details-card">

    <div class="details-heading">

      <div class="step">
        ENERGY YIELD
      </div>

      <h2>
        Renewable Energy Estimation
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">
        <small>Site Result</small>
        <strong id="detail-energy-site-result">—</strong>
      </div>


      <div class="detail">
        <small>Deployment Type</small>
        <strong id="detail-energy-deployment-type">—</strong>
      </div>


      <div class="detail">
        <small>Installed Capacity</small>
        <strong id="detail-energy-capacity">—</strong>
      </div>


      <div class="detail">
        <small>System Efficiency</small>
        <strong id="detail-system-efficiency">—</strong>
      </div>


      <div class="detail">
        <small>Annual Solar Energy</small>
        <strong id="detail-annual-solar-energy">—</strong>
      </div>


      <div class="detail">
        <small>Annual Wind Energy</small>
        <strong id="detail-annual-wind-energy">—</strong>
      </div>


      <div class="detail">
        <small>Total Annual Energy</small>
        <strong id="detail-total-energy">—</strong>
      </div>

    </div>

  </div>


  <!-- =====================================================
       FINANCIAL ANALYSIS
  ====================================================== -->

  <div class="details-card financial-card">

    <div class="details-heading">

      <div class="step">
        FINANCIAL ANALYSIS
      </div>

      <h2>
        Project Financial Overview
      </h2>

    </div>


    <div class="details-grid">

      <div class="detail">

        <small>
          Electricity Tariff
        </small>

        <strong id="financial-tariff">
          —
        </strong>

      </div>


      <div class="detail">

        <small>
          Annual Revenue
        </small>

        <strong id="financial-revenue">
          —
        </strong>

      </div>


      <div class="detail">

        <small>
          Installed Capacity
        </small>

        <strong id="financial-capacity">
          —
        </strong>

      </div>


      <div class="detail">

        <small>
          Cost Per MW
        </small>

        <strong id="financial-cost-mw">
          —
        </strong>

      </div>


      <div class="detail">

        <small>
          Estimated Project Cost
        </small>

        <strong id="financial-project-cost">
          —
        </strong>

      </div>


      <div class="detail">

        <small>
          Payback Period
        </small>

        <strong id="financial-payback">
          —
        </strong>

      </div>


      <div class="detail">

        <small>
          ROI
        </small>

        <strong id="financial-roi">
          —
        </strong>

      </div>

    </div>

  </div>

</section>


<footer>

  <strong>
    SolarWind AI
  </strong>

  <span>
    Intelligent Renewable Energy Planning • 2026
  </span>

</footer>
`;


/* =========================================================
   MAP
========================================================= */

const map = L.map("map", {

  center: [
    22.5937,
    78.9629
  ],

  zoom: 5,

  minZoom: 4,

  maxZoom: 12

});


L.tileLayer(
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  {
    attribution:
      "&copy; OpenStreetMap contributors"
  }
).addTo(map);


let selectedMarker = null;


/* =========================================================
   MAP CLICK
========================================================= */

map.on("click", (event) => {

  const latitude =
    event.latlng.lat.toFixed(6);

  const longitude =
    event.latlng.lng.toFixed(6);


  document.getElementById(
    "latitude"
  ).value = latitude;


  document.getElementById(
    "longitude"
  ).value = longitude;


  if (selectedMarker) {

    map.removeLayer(
      selectedMarker
    );

  }


  selectedMarker =
    L.marker([
      event.latlng.lat,
      event.latlng.lng
    ])
      .addTo(map)
      .bindPopup(`
        <strong>Selected Site</strong>
        <br>
        Latitude: ${latitude}
        <br>
        Longitude: ${longitude}
      `)
      .openPopup();


  const message =
    document.getElementById(
      "location-message"
    );


  message.textContent =
    "✓ Location selected successfully.";


  message.className =
    "location-message success";

});


/* =========================================================
   ANALYZE SITE
   KEEPING YOUR WORKING CODE UNCHANGED
========================================================= */

document
  .getElementById("analyze-button")
  .addEventListener(
    "click",
    async () => {

      const latitude =
        document.getElementById(
          "latitude"
        ).value;


      const longitude =
        document.getElementById(
          "longitude"
        ).value;


      if (
        !latitude ||
        !longitude
      ) {

        const message =
          document.getElementById(
            "location-message"
          );


        message.textContent =
          "⚠ Please select a location on the map first.";


        message.className =
          "location-message warning";


        return;

      }


      const button =
        document.getElementById(
          "analyze-button"
        );


      button.disabled = true;

      button.textContent =
        "Analyzing Site...";


      try {

        /*
        =====================================================
        BACKEND CONNECTION

        FastAPI POST /analysis/ expects JSON body:

        {
          "latitude": number,
          "longitude": number
        }

        =====================================================
        */

        const response =
          await fetch(
            "http://127.0.0.1:8000/analysis/",
            {
              method: "POST",

              headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
              },

              body: JSON.stringify({

                latitude:
                  Number(latitude),

                longitude:
                  Number(longitude)

              })

            }
          );


        /* ===================================================
           CHECK RESPONSE
        =================================================== */

        if (!response.ok) {

          const errorText =
            await response.text();

          console.error(
            "Backend error:",
            errorText
          );


          throw new Error(
            `Backend returned ${response.status}: ${errorText}`
          );

        }


        /* ===================================================
           READ JSON RESPONSE
        =================================================== */

        const data =
          await response.json();


        console.log(
          "BACKEND RESPONSE:",
          data
        );


        /* ===================================================
           SHOW RESULTS
        =================================================== */

        showResults(
          latitude,
          longitude,
          data
        );


      } catch (error) {

        console.error(
          "Analysis error:",
          error
        );


        alert(
          "Analysis request failed. Please check the FastAPI terminal for the exact error."
        );


      } finally {

        button.disabled = false;

        button.textContent =
          "Analyze Site →";

      }

    }
  );


/* =========================================================
   RESULTS
========================================================= */

function showResults(
  latitude,
  longitude,
  data
) {

  document
    .getElementById("home")
    .classList.add("hidden");


  document
    .getElementById("results-page")
    .classList.remove("hidden");


  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });


  /* =====================================================
     LOCATION
  ===================================================== */

  document
    .getElementById(
      "result-location"
    )
    .textContent =
    `${latitude}°, ${longitude}°`;


  document
    .getElementById(
      "detail-latitude"
    )
    .textContent =
    `${latitude}°`;


  document
    .getElementById(
      "detail-longitude"
    )
    .textContent =
    `${longitude}°`;


  /* =====================================================
     SOLAR
  ===================================================== */

  const solar =
    data?.solar_assessment?.solar_irradiance;


  document
    .getElementById(
      "solar-result"
    )
    .textContent =
    solar !== undefined
      ? `${Number(solar).toFixed(2)} kWh/m²/day`
      : "—";


  /* =====================================================
     WIND
  ===================================================== */

  const wind =
    data?.wind_assessment?.wind_speed;


  document
    .getElementById(
      "wind-result"
    )
    .textContent =
    wind !== undefined
      ? `${Number(wind).toFixed(2)} m/s`
      : "—";


  /* =====================================================
     OVERALL SCORE
  ===================================================== */

  const score =
    data?.site_suitability?.overall_score;


  document
    .getElementById(
      "score-result"
    )
    .textContent =
    score !== undefined
      ? `${Number(score).toFixed(1)}/100`
      : "—";


  /* =====================================================
     ANNUAL ENERGY
  ===================================================== */

  const energy =
    data
      ?.energy_yield
      ?.total_estimated_annual_energy;


  document
    .getElementById(
      "energy-result"
    )
    .textContent =
    energy !== undefined
      ? `${Number(energy).toFixed(2)} MWh/year`
      : "—";


  /* =====================================================
     WIND CLASS
  ===================================================== */

  const windClass =
    data
      ?.wind_assessment
      ?.wind_class;


  document
    .getElementById(
      "detail-wind-class"
    )
    .textContent =
    windClass || "—";


  /* =====================================================
     CAPACITY FACTOR
  ===================================================== */

  const capacityFactor =
    data
      ?.wind_assessment
      ?.capacity_factor;


  document
    .getElementById(
      "detail-capacity-factor"
    )
    .textContent =
    capacityFactor !== undefined
      ? `${Number(capacityFactor) * 100}%`
      : "—";


  /* =====================================================
     ML ENERGY PREDICTION
  ===================================================== */

  const prediction =
    data
      ?.ml_energy_prediction
      ?.energy_prediction;


  document
    .getElementById(
      "detail-prediction"
    )
    .textContent =
    prediction !== undefined
      ? Number(prediction).toFixed(2)
      : "—";


  /* =====================================================
     DEPLOYMENT
  ===================================================== */

  const deployment =
    data?.recommended_deployment;


  if (deployment) {

    document
      .getElementById(
        "detail-deployment"
      )
      .textContent =
      `${deployment.recommended_technology} — ${deployment.recommended_capacity} MW`;

  } else {

    document
      .getElementById(
        "detail-deployment"
      )
      .textContent =
      "—";

  }


  /* =====================================================
     ENVIRONMENTAL DATA
  ===================================================== */

  const environmental =
    data?.environmental_data;


  if (environmental) {

    document.getElementById(
      "detail-solar-irradiance"
    ).textContent =
      environmental.solar_irradiance !== undefined
        ? `${Number(environmental.solar_irradiance).toFixed(2)} kWh/m²/day`
        : "—";


    document.getElementById(
      "detail-temperature"
    ).textContent =
      environmental.temperature !== undefined
        ? `${Number(environmental.temperature).toFixed(2)} °C`
        : "—";


    document.getElementById(
      "detail-humidity"
    ).textContent =
      environmental.relative_humidity !== undefined
        ? `${Number(environmental.relative_humidity).toFixed(2)} %`
        : "—";


    document.getElementById(
      "detail-elevation"
    ).textContent =
      environmental.elevation !== undefined
        ? `${Number(environmental.elevation).toFixed(2)} m`
        : "—";


    document.getElementById(
      "detail-slope"
    ).textContent =
      environmental.slope !== undefined
        ? `${Number(environmental.slope).toFixed(2)}°`
        : "—";


    document.getElementById(
      "detail-wind-speed"
    ).textContent =
      environmental.wind_speed !== undefined
        ? `${Number(environmental.wind_speed).toFixed(2)} m/s`
        : "—";


    document.getElementById(
      "detail-power-density"
    ).textContent =
      environmental.power_density !== undefined
        ? `${Number(environmental.power_density).toFixed(2)} W/m²`
        : "—";


    document.getElementById(
      "detail-total-roads"
    ).textContent =
      environmental.total_roads !== undefined
        ? environmental.total_roads
        : "—";


    document.getElementById(
      "detail-road-types"
    ).textContent =
      environmental.unique_road_types !== undefined
        ? environmental.unique_road_types
        : "—";


    document.getElementById(
      "detail-distance-road"
    ).textContent =
      environmental.distance_to_road !== undefined
        ? `${Number(environmental.distance_to_road).toFixed(2)} km`
        : "—";


    document.getElementById(
      "detail-distance-grid"
    ).textContent =
      environmental.distance_to_grid !== undefined
        ? `${Number(environmental.distance_to_grid).toFixed(2)} km`
        : "—";


    document.getElementById(
      "detail-accessibility"
    ).textContent =
      environmental.accessibility || "—";


    document.getElementById(
      "detail-land-area"
    ).textContent =
      environmental.land_area !== undefined
        ? `${Number(environmental.land_area).toFixed(2)} acres`
        : "—";

  }


  /* =====================================================
     SITE SUITABILITY BREAKDOWN
  ===================================================== */

  const suitability =
    data?.site_suitability;


  if (suitability) {

    document.getElementById(
      "detail-renewable-score"
    ).textContent =
      suitability.renewable_score !== undefined
        ? `${Number(suitability.renewable_score).toFixed(2)}/100`
        : "—";


    document.getElementById(
      "detail-terrain-score"
    ).textContent =
      suitability.terrain_score !== undefined
        ? `${Number(suitability.terrain_score).toFixed(2)}/100`
        : "—";


    document.getElementById(
      "detail-infrastructure-score"
    ).textContent =
      suitability.infrastructure_score !== undefined
        ? `${Number(suitability.infrastructure_score).toFixed(2)}/100`
        : "—";


    document.getElementById(
      "detail-environmental-score"
    ).textContent =
      suitability.environmental_score !== undefined
        ? `${Number(suitability.environmental_score).toFixed(2)}/100`
        : "—";


    document.getElementById(
      "detail-economic-score"
    ).textContent =
      suitability.economic_score !== undefined
        ? `${Number(suitability.economic_score).toFixed(2)}/100`
        : "—";


    document.getElementById(
      "detail-overall-score"
    ).textContent =
      suitability.overall_score !== undefined
        ? `${Number(suitability.overall_score).toFixed(2)}/100`
        : "—";

  }


  /* =====================================================
     TECHNICAL FEASIBILITY
  ===================================================== */

  const feasibility =
    data?.technical_feasibility;


  if (feasibility) {

    document.getElementById(
      "detail-feasibility-status"
    ).textContent =
      feasibility.status === true
        ? "APPROVED"
        : "NOT APPROVED";


    document.getElementById(
      "detail-feasibility-score"
    ).textContent =
      feasibility.score !== undefined
        ? `${Number(feasibility.score).toFixed(0)}/100`
        : "—";


    const constraints =
      feasibility.constraint_summary;


    if (constraints) {

      document.getElementById(
        "detail-feasibility-grid"
      ).textContent =
        constraints.distance_to_grid !== undefined
          ? `${Number(constraints.distance_to_grid).toFixed(2)} km`
          : "—";


      document.getElementById(
        "detail-feasibility-road"
      ).textContent =
        constraints.distance_to_road !== undefined
          ? `${Number(constraints.distance_to_road).toFixed(2)} km`
          : "—";


      document.getElementById(
        "detail-feasibility-accessibility"
      ).textContent =
        constraints.accessibility || "—";

    }

  }


  /* =====================================================
     ML PREDICTION DETAILS
  ===================================================== */

  const ml =
    data?.ml_energy_prediction;


  if (ml) {

    document.getElementById(
      "detail-ml-energy"
    ).textContent =
      ml.energy_prediction !== undefined
        ? `${Number(ml.energy_prediction).toFixed(2)}`
        : "—";


    const explanation =
      ml.explanation;


    if (explanation) {

      const topFeatures =
        explanation.top_features || [];


      document.getElementById(
        "detail-primary-driver"
      ).textContent =
        topFeatures[0] || "—";


      document.getElementById(
        "detail-secondary-driver"
      ).textContent =
        topFeatures[1] || "—";


      document.getElementById(
        "detail-ml-message"
      ).textContent =
        explanation.message || "—";

    }

  }


  /* =====================================================
     DEPLOYMENT RECOMMENDATION DETAILS
  ===================================================== */

  if (deployment) {

    document.getElementById(
      "detail-recommended-technology"
    ).textContent =
      deployment.recommended_technology || "—";


    document.getElementById(
      "detail-recommended-capacity"
    ).textContent =
      deployment.recommended_capacity !== undefined
        ? `${deployment.recommended_capacity} MW`
        : "—";


    document.getElementById(
      "detail-expansion-status"
    ).textContent =
      deployment.expansion_status || "—";


    document.getElementById(
      "detail-optimization-remarks"
    ).textContent =
      deployment.optimization_remarks || "—";

  }


  /* =====================================================
     ENERGY YIELD DETAILS
  ===================================================== */

  const energyYield =
    data?.energy_yield;


  if (energyYield) {

    document.getElementById(
      "detail-energy-site-result"
    ).textContent =
      energyYield.site_result || "—";


    document.getElementById(
      "detail-energy-deployment-type"
    ).textContent =
      energyYield.deployment_type || "—";


    document.getElementById(
      "detail-energy-capacity"
    ).textContent =
      energyYield.installed_capacity !== undefined
        ? `${energyYield.installed_capacity} MW`
        : "—";


    document.getElementById(
      "detail-system-efficiency"
    ).textContent =
      energyYield.system_efficiency !== undefined
        ? `${Number(energyYield.system_efficiency * 100).toFixed(1)}%`
        : "—";


    document.getElementById(
      "detail-annual-solar-energy"
    ).textContent =
      energyYield.estimated_annual_solar_energy !== undefined
        ? `${Number(energyYield.estimated_annual_solar_energy).toFixed(2)} MWh/year`
        : "—";


    document.getElementById(
      "detail-annual-wind-energy"
    ).textContent =
      energyYield.estimated_annual_wind_energy !== undefined
        ? `${Number(energyYield.estimated_annual_wind_energy).toFixed(2)} MWh/year`
        : "—";


    document.getElementById(
      "detail-total-energy"
    ).textContent =
      energyYield.total_estimated_annual_energy !== undefined
        ? `${Number(energyYield.total_estimated_annual_energy).toFixed(2)} MWh/year`
        : "—";

  }


  /* =====================================================
     FINANCIAL RESULTS
  ===================================================== */

  const financial =
    data?.financial_metrics;


  if (financial) {

    /* TARIFF */

    document
      .getElementById(
        "financial-tariff"
      )
      .textContent =
      `₹${Number(
        financial.electricity_tariff
      ).toFixed(2)} / kWh`;


    /* REVENUE */

    document
      .getElementById(
        "financial-revenue"
      )
      .textContent =
      `₹${Number(
        financial.annual_revenue
      ).toLocaleString(
        "en-IN",
        {
          maximumFractionDigits: 2
        }
      )}`;


    /* CAPACITY */

    document
      .getElementById(
        "financial-capacity"
      )
      .textContent =
      `${financial.installed_capacity_mw} MW`;


    /* COST PER MW */

    document
      .getElementById(
        "financial-cost-mw"
      )
      .textContent =
      `₹${Number(
        financial.cost_per_mw
      ).toLocaleString("en-IN")}`;


    /* PROJECT COST */

    document
      .getElementById(
        "financial-project-cost"
      )
      .textContent =
      `₹${Number(
        financial.estimated_project_cost
      ).toLocaleString("en-IN")}`;


    /* PAYBACK */

    document
      .getElementById(
        "financial-payback"
      )
      .textContent =
      `${Number(
        financial.payback_period
      ).toFixed(2)} years`;


    /* ROI */

    document
      .getElementById(
        "financial-roi"
      )
      .textContent =
      `${(
        Number(financial.roi) * 100
      ).toFixed(2)}%`;

  }

}


/* =========================================================
   BACK BUTTON
========================================================= */

document
  .getElementById(
    "back-button"
  )
  .addEventListener(
    "click",
    () => {

      document
        .getElementById(
          "results-page"
        )
        .classList.add(
          "hidden"
        );


      document
        .getElementById(
          "home"
        )
        .classList.remove(
          "hidden"
        );


      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });

    }
  );