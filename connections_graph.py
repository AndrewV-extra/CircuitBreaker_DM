# connections_graph.py
from streamlit_agraph import agraph, Node, Edge, Config

_obsidian_json = {
    "nodes": [
        {
            "id": "ab1b91cc17a26257",
            "type": "text",
            "text": "Covid-19",
            "x": -125,
            "y": -30,
            "width": 250,
            "height": 60,
        },
        {
            "id": "e9dd69c751da8bf8",
            "type": "text",
            "text": "Pressure on healthcare systems",
            "x": -125,
            "y": -180,
            "width": 250,
            "height": 60,
        },
        {
            "id": "90bad0fdba0932ad",
            "type": "text",
            "text": "Access to healthcare",
            "x": -500,
            "y": -180,
            "width": 250,
            "height": 60,
        },
        {
            "id": "dde9d64a500477d7",
            "type": "text",
            "text": "Circuit Breaker",
            "x": -500,
            "y": -30,
            "width": 250,
            "height": 60,
        },
        {
            "id": "44c93b01890ae2f6",
            "type": "text",
            "text": "Balanced lifestyle",
            "x": -500,
            "y": 120,
            "width": 250,
            "height": 60,
        },
        {
            "id": "673100c081019a13",
            "type": "text",
            "text": "Wellbeing of DM Patients",
            "x": -880,
            "y": -30,
            "width": 250,
            "height": 60,
        },
        {
            "id": "577f3fbf32436649",
            "type": "text",
            "text": "Prevalence of DM 2",
            "x": -125,
            "y": 120,
            "width": 250,
            "height": 60,
        },
        # ✅ New node
        {
            "id": "active_sg_circle",
            "type": "text",
            "text": "Active SG Circle",
            "x": -880,
            "y": 120,
            "width": 250,
            "height": 60,
        },
    ],
    "edges": [
        {
            "id": "b45b040aa5ab92cb",
            "fromNode": "ab1b91cc17a26257",
            "fromSide": "top",
            "toNode": "e9dd69c751da8bf8",
            "toSide": "bottom",
            "label": "+",
        },
        {
            "id": "57bcecf7e225dffa",
            "fromNode": "e9dd69c751da8bf8",
            "fromSide": "left",
            "toNode": "90bad0fdba0932ad",
            "toSide": "right",
            "label": "-",
        },
        {
            "id": "aede1fedd79e0c7c",
            "fromNode": "ab1b91cc17a26257",
            "fromSide": "left",
            "toNode": "dde9d64a500477d7",
            "toSide": "right",
            "label": "+",
        },
        {
            "id": "9b1ae8b55464d4b4",
            "fromNode": "dde9d64a500477d7",
            "fromSide": "top",
            "toNode": "90bad0fdba0932ad",
            "toSide": "bottom",
            "label": "-",
        },
        {
            "id": "b1f1940011e509e9",
            "fromNode": "dde9d64a500477d7",
            "fromSide": "bottom",
            "toNode": "44c93b01890ae2f6",
            "toSide": "top",
            "label": "-",
        },
        {
            "id": "274a6e34ea84db2b",
            "fromNode": "44c93b01890ae2f6",
            "fromSide": "right",
            "toNode": "577f3fbf32436649",
            "toSide": "left",
            "label": "-",
        },
        {
            "id": "908d6b2c8e9f506d",
            "fromNode": "90bad0fdba0932ad",
            "fromSide": "left",
            "toNode": "673100c081019a13",
            "toSide": "right",
            "label": "+",
        },
        {
            "id": "ff9e44334520470a",
            "fromNode": "dde9d64a500477d7",
            "fromSide": "left",
            "toNode": "673100c081019a13",
            "toSide": "right",
            "label": "-",
        },
        {
            "id": "6e8ac7696f361774",
            "fromNode": "44c93b01890ae2f6",
            "fromSide": "left",
            "toNode": "673100c081019a13",
            "toSide": "right",
            "label": "+",
        },
        # ✅ New edge (green on hover)
        {
            "id": "edge_active_sg",
            "fromNode": "active_sg_circle",
            "fromSide": "right",
            "toNode": "44c93b01890ae2f6",
            "toSide": "left",
            "label": "+",
        },
    ],
}


def render(height=350):
    """Parses the Obsidian JSON and renders a beautifully styled agraph component."""
    nodes = []
    edges = []

    # Streamlit & Obsidian Hybrid Styling
    STREAMLIT_SECONDARY_BG = "#262730"
    STREAMLIT_BORDER = "#4B4C53"
    STREAMLIT_PRIMARY = "#FF4B4B"
    TEXT_COLOR = "#FAFAFA"

    # Highlight Colors for +/- edges
    COLOR_POSITIVE = "#21c354"
    COLOR_NEGATIVE = "#FF4B4B"

    # Convert Nodes
    for n in _obsidian_json["nodes"]:
        nodes.append(
            Node(
                id=n["id"],
                label=n["text"],
                title="",
                shape="box",
                x=n["x"],
                y=n["y"],
                widthConstraint={"minimum": 200, "maximum": 250},
                margin=15,
                shapeProperties={"borderRadius": 8},
                color={
                    "background": STREAMLIT_SECONDARY_BG,
                    "border": STREAMLIT_BORDER,
                    "highlight": {
                        "background": STREAMLIT_PRIMARY,
                        "border": STREAMLIT_PRIMARY,
                    },
                    "hover": {
                        "background": "#343540",
                        "border": "#343540",
                    },
                },
                font={"color": TEXT_COLOR, "face": "sans-serif", "size": 14},
            )
        )

    # Convert Edges
    for e in _obsidian_json["edges"]:
        edge_label = e.get("label", "")
        if edge_label == "+":
            interaction_color = COLOR_POSITIVE
        elif edge_label == "-":
            interaction_color = COLOR_NEGATIVE
        else:
            interaction_color = STREAMLIT_PRIMARY

        edges.append(
            Edge(
                source=e["fromNode"],
                target=e["toNode"],
                arrows="to",
                width=2,
                smooth={"type": "cubicBezier", "roundness": 0.5},
                color={
                    "color": "#808495",
                    "highlight": interaction_color,
                    "hover": interaction_color,
                },
            )
        )

    # Graph Config
    config = Config(
        width="100%",
        height=height,
        directed=True,
        physics=False,
        hierarchical=False,
        interaction={
            "hover": True,
            "selectConnectedEdges": True,
            "zoomView": True,
            "dragView": True,
        },
    )

    return agraph(nodes=nodes, edges=edges, config=config)
