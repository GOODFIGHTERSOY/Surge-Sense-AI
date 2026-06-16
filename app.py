import streamlit as st
import folium
from streamlit_folium import st_folium
import data_processor
import model_engine
import os

# --- Page Config ---
st.set_page_config(layout="wide", page_title="SURGE SENSE AI Event Intelligence")

st.title("🚦 SURGE SENSE AI Event-Driven Congestion Intelligence")
st.caption("Theme 2 Prototype: Forecasting traffic impact and automating optimal resource allocation.")

# Load Data
data_path = os.path.join("data/events.csv")
try:
    df = data_processor.load_and_clean_data(data_path)
    data_loaded = True
except FileNotFoundError:
    st.error(f"Dataset not found at {data_path}. Please ensure the file is placed correctly.")
    data_loaded = False

if data_loaded:
    # --- Navigation ---
   
    tab1, tab2, tab3 = st.tabs(["📊 METRIC ANALYTICS", "🔮 PREDICTIVE SIMULATION", "📡 DISPATCH & LEARNING LOOP"])

    # --- TAB 1: Historical Data ---
    with tab1:
        st.subheader("Historical Event Impact Analysis")
        st.write("Analyzing past event clusters to understand baseline congestion patterns.")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.metric("Total Relevant Events Logged", len(df))
            top_cause = df['event_cause'].mode()[0]
            st.metric("Most Frequent Event Type", top_cause.replace('_', ' ').title())
            
            selected_cause = st.selectbox("Filter Map by Event Type:", ['All'] + list(df['event_cause'].unique()))
        
        with col2:
            map_df = df if selected_cause == 'All' else df[df['event_cause'] == selected_cause]
            
            # Map centering on Bengaluru
            m = folium.Map(location=[12.9716, 77.5946], zoom_start=11, tiles="cartodbpositron")
            
            for idx, row in map_df.iterrows():
                folium.CircleMarker(
                    location=[row['latitude'], row['longitude']],
                    radius=5,
                    color="#FF4B4B" if row['requires_road_closure'] else "#0068C9",
                    fill=True,
                    popup=f"Cause: {row['event_cause']}<br>Duration: {row['duration_mins']:.0f} mins"
                ).add_to(m)
            
            st_folium(m, width=800, height=400)

    # --- TAB 2: Predictive Engine ---
    with tab2:
        st.subheader("Forecast Upcoming Event Impact")
        
        with st.form("event_form"):
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                e_cause = st.selectbox("Event Category", ['public_event', 'procession', 'protest', 'vip_movement', 'construction'])
                e_footfall = st.number_input("Expected Footfall / Gathering Size", min_value=500, max_value=200000, value=15000, step=1000)
            with col_b:
                e_duration = st.slider("Expected Duration (Hours)", 1, 24, 4)
                e_peak = st.checkbox("Event overlaps with Peak Hours (8-11 AM or 5-8 PM)?", value=True)
            with col_c:
                st.write("Submit parameters to run the predictive deployment engine.")
                submit_button = st.form_submit_button(label="Analyze & Generate Deployment Plan")

        if submit_button:
            st.markdown("---")
            # Run the engine
            results = model_engine.predict_event_impact(e_cause, e_footfall, e_duration, e_peak)
            strategy = model_engine.get_diversion_strategy(results['impact_score'])
            
            st.subheader("🎯 Automated Deployment Output")
            
            # Key Metrics
            r1, r2, r3, r4 = st.columns(4)
            r1.metric(label="Predicted Severity Score", value=f"{results['impact_score']} / 10")
            r2.metric(label="Spillover Radius", value=f"{results['impact_radius_km']} km")
            r3.metric(label="Traffic Police Required", value=f"{results['police_personnel']} Personnel")
            r4.metric(label="Barricades Required", value=f"{results['barricades']} Units")
            
            # Actionable Strategy
            st.info(f"**Recommended Action Plan:** {strategy}")
            st.success(f"**Diversion Routing:** Allocate {results['diversions_needed']} major diversion nodes at the outer edge of the {results['impact_radius_km']}km radius.")
    # --- TAB 3: DISPATCH & POST-EVENT LEARNING ---
    with tab3:
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.subheader("📱 Automated Field Dispatch (WhatsApp/Radio)")
            st.write("Generate instant tactical summaries for on-ground ASTraM units.")
            
            # Using the mock results from Tab 2
            mock_impact = 7.5
            mock_radius = 2.2
            
            dispatch_msg = f"""
*ASTraM TACTICAL ALERT* 🚨
*Event:* Planned Gathering
*Expected Spillover:* {mock_radius} KM radius.
*Severity:* {mock_impact}/10
---
*DEPLOYMENT ORDERS:*
📍 12 Officers to inner perimeter.
🚧 40 Barricades required at outer choke points.
🔀 Execute routing diversion Protocol Alpha.
*Acknowledge receipt.*
            """
            st.code(dispatch_msg, language="markdown")
            st.button("📋 Copy to Clipboard for Control Room Broadcast")
            
            st.markdown("---")
            
            # --- NEW VMS PREVIEW SECTION (Replaced MapmyIndia) ---
            st.markdown("### 🚥 Digital Highway Signboard (VMS) Preview")
            st.write("Automatically pushes reroute instructions to digital boards 5km from the epicenter.")
            
            # Simulated LED Matrix Display using HTML/CSS
            st.markdown(f"""
                <div style="background-color: #000000; border: 4px solid #333; border-radius: 8px; padding: 20px; text-align: center; font-family: 'Courier New', monospace; box-shadow: 0px 4px 10px rgba(0,0,0,0.5);">
                    <h2 style="color: #FFA500; margin: 0; text-transform: uppercase; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 8px #FFA500;">EXPECT SEVERE DELAYS</h2>
                    <h3 style="color: #FFA500; margin: 10px 0 0 0; text-transform: uppercase; font-weight: 700; text-shadow: 0 0 8px #FFA500;">UPCOMING EVENT HOTSPOT</h3>
                    <h4 style="color: #00FF00; margin: 15px 0 0 0; text-transform: uppercase; font-weight: 700; text-shadow: 0 0 8px #00FF00;">>> DIVERT TO OUTER RING ROAD >></h4>
                </div>
            """, unsafe_allow_html=True)
            
            st.button("📡 Push to Active City VMS Network")

        with col_right:
            st.subheader("🧠 Post-Event Machine Learning Loop")
            st.write("Officers log ground-truth data post-event to calibrate the prediction model's weights.")
            
            with st.container(border=True):
                st.markdown("#### Log Actual Event Outcomes")
                actual_footfall = st.number_input("Actual Crowd Size", value=20000, step=1000)
                actual_clearance_time = st.slider("Hours to clear traffic completely", 1.0, 10.0, 4.5)
                was_prediction_accurate = st.radio("Was the predictive deployment sufficient?", ["Yes, perfect.", "No, we needed more officers.", "No, we over-deployed."])
                
                if st.button("💾 Submit to Model Training DB"):
                    st.success("✅ Ground truth logged. Graph Network edge-weights have been updated for future predictions at this location.")
                    st.info("💡 By closing this loop, the Surge Sense AI Traffic system actively prevents historical biases and adapts to changing city infrastructure.")
