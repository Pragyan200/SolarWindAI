import "./App.css";

function App() {
  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">
          <span className="logo-icon">☀</span>
          <span>SolarWind<span className="ai">AI</span></span>
        </div>

        <nav>
          <a href="#dashboard">Dashboard</a>
          <a href="#analysis">Site Analysis</a>
          <a href="#about">About</a>
        </nav>
      </header>

      <main>
        <section className="hero" id="dashboard">
          <div className="hero-content">
            <p className="tag">RENEWABLE ENERGY INTELLIGENCE</p>

            <h1>
              Smart Renewable
              <br />
              <span>Energy Planning</span>
            </h1>

            <p className="hero-text">
              Analyze solar and wind potential, evaluate site feasibility,
              estimate energy production, and plan renewable energy
              deployment with AI-powered analysis.
            </p>

            <button
              className="primary-button"
              onClick={() =>
                document
                  .getElementById("analysis")
                  .scrollIntoView({ behavior: "smooth" })
              }
            >
              Start Site Analysis →
            </button>
          </div>

          <div className="hero-card">
            <div className="sun">☀</div>
            <div className="wind">≋</div>

            <div className="energy-card">
              <span>RENEWABLE POTENTIAL</span>
              <strong>AI POWERED</strong>
            </div>
          </div>
        </section>

        <section className="features">
          <div className="feature-card">
            <div className="feature-icon">☀</div>
            <h3>Solar Analysis</h3>
            <p>
              Analyze solar irradiance and estimate solar energy potential.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">≋</div>
            <h3>Wind Analysis</h3>
            <p>
              Evaluate wind speed, wind class and wind energy potential.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">✓</div>
            <h3>Site Feasibility</h3>
            <p>
              Determine whether a location is technically suitable for
              renewable deployment.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Energy Prediction</h3>
            <p>
              Predict annual renewable energy production using AI models.
            </p>
          </div>
        </section>

        <section className="analysis-section" id="analysis">
          <div className="section-heading">
            <p className="tag">SITE ANALYSIS</p>
            <h2>Analyze Your Site</h2>
            <p>
              Enter the site information below to evaluate renewable energy
              potential.
            </p>
          </div>

          <div className="analysis-card">
            <div className="form-grid">
              <div className="input-group">
                <label>Latitude</label>
                <input type="number" placeholder="e.g. 20.2961" />
              </div>

              <div className="input-group">
                <label>Longitude</label>
                <input type="number" placeholder="e.g. 85.8245" />
              </div>

              <div className="input-group">
                <label>Land Area (acres)</label>
                <input type="number" placeholder="e.g. 10" />
              </div>

              <div className="input-group">
                <label>Available Land (acres)</label>
                <input type="number" placeholder="e.g. 8" />
              </div>

              <div className="input-group">
                <label>Slope (°)</label>
                <input type="number" placeholder="e.g. 5" />
              </div>

              <div className="input-group">
                <label>Distance to Grid (km)</label>
                <input type="number" placeholder="e.g. 2" />
              </div>

              <div className="input-group">
                <label>Distance to Road (km)</label>
                <input type="number" placeholder="e.g. 1" />
              </div>

              <div className="input-group">
                <label>Accessibility</label>
                <select>
                  <option value="">Select accessibility</option>
                  <option value="Good">Good</option>
                  <option value="Moderate">Moderate</option>
                  <option value="Poor">Poor</option>
                </select>
              </div>
            </div>

            <div className="checkbox-group">
              <input type="checkbox" id="restricted" />
              <label htmlFor="restricted">
                Site contains restricted land
              </label>
            </div>

            <button className="analyze-button">
              Analyze Site
            </button>
          </div>
        </section>

        <section className="results-section">
          <div className="section-heading">
            <p className="tag">ANALYSIS RESULTS</p>
            <h2>Your Renewable Energy Results</h2>
          </div>

          <div className="results-grid">
            <div className="result-card">
              <span>FEASIBILITY</span>
              <h3>—</h3>
              <p>Waiting for analysis</p>
            </div>

            <div className="result-card">
              <span>OVERALL SCORE</span>
              <h3>—</h3>
              <p>Out of 100</p>
            </div>

            <div className="result-card">
              <span>ENERGY POTENTIAL</span>
              <h3>—</h3>
              <p>Annual prediction</p>
            </div>

            <div className="result-card">
              <span>WIND CLASS</span>
              <h3>—</h3>
              <p>Site classification</p>
            </div>
          </div>
        </section>
      </main>

      <footer id="about">
        <div>
          <strong>SolarWindAI</strong>
          <p>
            AI-powered solar and wind energy site analysis.
          </p>
        </div>

        <p>© 2026 SolarWindAI</p>
      </footer>
    </div>
  );
}

export default App;