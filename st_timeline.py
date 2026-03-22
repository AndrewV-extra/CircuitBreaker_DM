import streamlit as st


def st_timeline(events, height=400):
    """
    Renders a vertical scrollable timeline.

    :param events: List of dictionaries containing 'date', 'title', and 'description'.
    :param height: Max height of the scrollable container in pixels.
    """

    # CSS styling
    css = f"""
    <style>
        .timeline-container {{
            max-height: {height}px;
            overflow-y: auto;
            padding: 10px 20px;
            border-radius: 8px;
            background-color: rgba(128, 128, 128, 0.05);
        }}
        .timeline {{
            position: relative;
            border-left: 2px solid #FF4B4B;
            margin-left: 10px;
            padding-left: 25px;
            padding-bottom: 10px;
        }}
        .timeline-event {{
            position: relative;
            margin-bottom: 30px;
        }}
        .timeline-circle {{
            position: absolute;
            width: 14px;
            height: 14px;
            background-color: #FF4B4B;
            border: 2px solid white;
            border-radius: 50%;
            left: -33px;
            top: 5px;
        }}
        .timeline-date {{
            font-size: 0.85em;
            color: #888;
            font-weight: 600;
            margin-bottom: 4px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .timeline-title {{
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .timeline-desc {{
            font-size: 0.95em;
            opacity: 0.8;
            line-height: 1.4;
        }}
        .timeline-container::-webkit-scrollbar {{
            width: 8px;
        }}
        .timeline-container::-webkit-scrollbar-track {{
            background: transparent;
        }}
        .timeline-container::-webkit-scrollbar-thumb {{
            background-color: rgba(128, 128, 128, 0.3);
            border-radius: 4px;
        }}
    </style>
    """

    # Generate HTML without indentation to prevent Markdown code block bugs
    html_events = ""
    for event in events:
        date = event.get("date", "")
        title = event.get("title", "")
        desc = event.get("description", "")

        # String concatenation without line-breaks/indents prevents Streamlit markdown issues
        html_events += f'<div class="timeline-event">'
        html_events += f'<div class="timeline-circle"></div>'
        html_events += f'<div class="timeline-date">{date}</div>'
        html_events += f'<div class="timeline-title">{title}</div>'
        html_events += f'<div class="timeline-desc">{desc}</div>'
        html_events += f"</div>"

    html = f'<div class="timeline-container"><div class="timeline">{html_events}</div></div>'

    # Render in Streamlit
    st.markdown(css + html, unsafe_allow_html=True)
