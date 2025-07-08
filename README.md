# 🚀 Deployment Risk Assessment System

An AI-powered deployment risk prediction and automated rollback system that helps teams make informed decisions about code deployments using machine learning.

## 📋 Overview

This system analyzes deployment characteristics and predicts the risk of requiring a rollback, helping development teams:
- **Prevent failed deployments** before they impact production
- **Automate risk assessment** using ML models
- **Monitor deployments** in real-time
- **Make data-driven decisions** about when to deploy
# 🚀 Deployment Risk Assessment System

A web-based tool that uses machine learning to predict deployment risks and help teams make informed decisions about software releases.

## Honest Project Status

**This is a demo/prototype project** - not a production-ready system. Here's what you need to know:

### What Works ✅
- **Frontend**: Beautiful, responsive UI with modern design
- **Backend**: FastAPI server with proper API endpoints
- **ML Pipeline**: Basic RandomForest model for risk prediction
- **Form Handling**: Complete deployment form with validation
- **Risk Visualization**: Interactive risk meter and metrics display
- **Fallback Logic**: If the ML model fails, uses rule-based calculation

### What's Mock/Limited ❌
- **Training Data**: Uses synthetic data, not real deployment histories
- **Model Accuracy**: Trained on artificial patterns, not validated on real deployments
- **Monitoring Charts**: Shows random/fake data, not connected to actual services
- **Deployment Logs**: Just a placeholder, no real logging system
- **Database**: No persistent storage - everything is in-memory


## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **ML**: scikit-learn (RandomForest)
- **Visualization**: Chart.js
- **Styling**: Custom CSS with modern design patterns


## 🎯 How It Works

1. **Input**: Fill out deployment details (files changed, test coverage, etc.)
2. **ML Prediction**: Model calculates risk score based on historical patterns
3. **Risk Assessment**: Categorizes as Safe/Monitor/Rollback/Block
4. **Visualization**: Shows risk meter and related metrics
5. **Decision Support**: Provides deployment recommendation

## 📊 Risk Factors

The model considers:
- **Files Changed**: More changes = higher risk
- **Test Coverage**: Lower coverage = higher risk  
- **Dependencies**: More dependencies = higher risk
- **Previous Failures**: Recent failures increase risk
- **Change Type**: Hotfixes are riskier than features
- **Deployment Time**: Night deployments are riskier

## 🎨 Features

- **Modern UI**: Clean, responsive design with animations
- **Real-time Analysis**: Instant risk calculation
- **Visual Feedback**: Color-coded risk meter
- **Tabbed Interface**: Deploy, Monitor, and Logs sections
- **Mobile Friendly**: Works on all device sizes

## 🔧 Making It Production-Ready

To use this in a real environment, you'd need to:

1. **Collect Real Data**: Gather actual deployment metrics and outcomes
2. **Retrain Model**: Use real historical data for training
3. **Add Persistence**: Implement proper database storage
4. **Connect CI/CD**: Integrate with Jenkins, GitLab CI, etc.
5. **Add Authentication**: Implement user management
6. **Real Monitoring**: Connect to actual service metrics

## ✨ Features

- **🎯 Risk Prediction**: ML-powered risk scoring based on deployment characteristics
- **📊 Real-time Monitoring**: Live charts showing latency and error rates
- **🔄 Automated Rollback**: Intelligent rollback recommendations
- **📱 Modern UI**: Responsive web interface with beautiful visualizations
- **⚡ Fast API**: Built with FastAPI for high-performance predictions
- **🎨 Interactive Dashboard**: Tabbed interface for deployment, monitoring, and logs

## 🏗️ Architecture

```
deployment-risk-system/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── model/
│   │   └── risk_model.pkl      # Trained ML model
│   ├── static/
│   │   └── styles.css          # Additional CSS (optional)
│   └── templates/
│       └── index.html          # Main web interface
├── train_model.py              # Model training script
├── generate_model.py           # Simple model generator
└── README.md                   # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd deployment-risk-system
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn scikit-learn pandas numpy jinja2 python-multipart
   ```

3. **Train the ML model**
   ```bash
   python train_model.py
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the web interface**
   ```
   http://localhost:8000
   ```

## 🤖 Model Training

The system uses a Random Forest classifier trained on deployment characteristics:

### Features Used:
- **Files Changed**: Number of files modified in the deployment
- **Test Coverage**: Percentage of code covered by tests
- **Dependencies**: Number of external dependencies
- **Previous Failures**: Count of recent deployment failures
- **Change Type**: Type of change (feature, bugfix, hotfix, refactor, config)
- **Deployment Time**: Time of day for deployment

### Training Process:
```bash
# Generate synthetic training data and train model
python train_model.py

# This creates app/model/risk_model.pkl
```

The model achieves good accuracy on synthetic data and can be retrained with real deployment data.

## 📊 Risk Scoring

The system provides risk scores from 0.0 to 1.0:

| Risk Score | Decision | Action |
|------------|----------|---------|
| 0.0 - 0.4 | ✅ Safe to Deploy | Proceed with deployment |
| 0.4 - 0.6 | ⚠️ Monitor Closely | Deploy with monitoring |
| 0.6 - 0.8 | 🔄 Rollback Required | Deploy with rollback ready |
| 0.8 - 1.0 | 🚫 Block Deployment | Do not deploy |

## 🔧 API Endpoints

### Prediction Endpoint
```http
POST /predict
Content-Type: application/json

{
  "files_changed": 15,
  "test_coverage": 85,
  "dependencies": 5,
  "previous_failures": 2,
  "change_type": "feature",
  "deployment_time": "afternoon"
}
```

**Response:**
```json
{
  "risk_score": 0.234,
  "latency": "317ms",
  "error_rate": 0.012,
  "anomaly": "Normal",
  "final_decision": "Safe to Deploy",
  "status": "proceed"
}
```

### Web Interface
```http
GET /
```
Returns the main dashboard interface.

## 📱 Web Interface

The web interface provides three main tabs:

1. **Deploy Tab**: Input deployment details and get risk analysis
2. **Monitor Tab**: Real-time monitoring charts (latency, error rates)
3. **Logs Tab**: Deployment history and logs (placeholder for future enhancement)

### Key Features:
- **Responsive Design**: Works on desktop and mobile
- **Real-time Charts**: Using Chart.js for monitoring visualization
- **Interactive Risk Meter**: Visual risk score representation
- **Form Validation**: Ensures all required fields are filled
- **Loading States**: Smooth user experience during API calls

## 🎯 Usage Examples

### Basic Risk Assessment
```bash
# Fill out the deployment form with:
- Service Name: user-service
- Change Type: feature
- Files Changed: 23
- Test Coverage: 78%
- Deployment Time: afternoon
- Dependencies: 8
- Previous Failures: 1

# Get risk analysis and deployment recommendation
```

### High-Risk Scenario
```bash
# Example high-risk deployment:
- Files Changed: 45+ (high impact)
- Test Coverage: <60% (low confidence)
- Change Type: hotfix (urgent)
- Deployment Time: night (risky)
- Previous Failures: 3+ (concerning pattern)

# Result: Risk Score > 0.8 → Block Deployment
```

## 🔄 Customization

### Adding New Features
1. **Update the model training** in `train_model.py`
2. **Modify the API** in `app/main.py` to handle new inputs
3. **Update the web form** in `app/templates/index.html`

### Integrating Real Data
Replace the synthetic data generation in `train_model.py` with your actual deployment data:

```python
# Instead of generate_data(), load your CSV:
df = pd.read_csv('your_deployment_data.csv')
```

### Custom Risk Thresholds
Modify the risk interpretation logic in `app/main.py`:

```python
# Adjust these thresholds based on your risk tolerance
if risk_score > 0.8:
    decision = "Block Deployment"
elif risk_score > 0.6:
    decision = "Rollback Required"
# ... etc
```

## 🚀 Production Deployment

### Docker Setup
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables
```bash
# Set in production
export MODEL_PATH="/app/model/risk_model.pkl"
export API_HOST="0.0.0.0"
export API_PORT="8000"
```

### Health Checks
The API includes basic health checking. For production, consider adding:
- Model validation endpoints
- Metrics collection (Prometheus)
- Logging integration
- Database connectivity for historical data

## 🧪 Testing

### Manual Testing
1. Start the application
2. Navigate to `http://localhost:8000`
3. Fill out the deployment form
4. Verify risk predictions make sense
5. Test different scenarios (high/low risk)

### API Testing
```bash
# Test prediction endpoint
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"files_changed": 10, "test_coverage": 80, "dependencies": 3, "previous_failures": 0, "change_type": "feature", "deployment_time": "morning"}'
```

## 📈 Monitoring & Metrics

The system tracks:
- **Total Deployments**: Count of risk assessments performed
- **High Risk Blocked**: Deployments prevented due to high risk
- **Auto Rollbacks**: Automated rollback recommendations
- **Success Rate**: Overall deployment success percentage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎉 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- ML powered by [scikit-learn](https://scikit-learn.org/)
- Charts using [Chart.js](https://www.chartjs.org/)
- Modern CSS design patterns

---
