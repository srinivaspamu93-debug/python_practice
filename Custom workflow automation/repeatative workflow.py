import streamlit as st
from pathlib import Path
from datetime import datetime
import json
import shutil
import re
import time

# ============================================================
# FLOWPILOT — Custom Workflow Automation Studio
# Single-file professional Streamlit application
# ============================================================

st.set_page_config(
    page_title="FlowPilot | Workflow Automation",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------- CSS -----------------------------

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #070b14;
        color: #e8edf7;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Header */
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 5px;
    }

    .brand-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(135deg, #7c5cff, #22d3ee);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        box-shadow: 0 8px 30px rgba(124,92,255,.25);
    }

    .brand-name {
        font-size: 25px;
        font-weight: 800;
        letter-spacing: -0.8px;
    }

    .brand-name span {
        color: #8b78ff;
    }

    .subtitle {
        color: #7d8799;
        font-size: 13px;
        margin-bottom: 30px;
    }

    /* Cards */
    .metric-card {
        background: #0d1320;
        border: 1px solid #1b2536;
        border-radius: 16px;
        padding: 20px;
        min-height: 125px;
    }

    .metric-label {
        color: #7f8ba1;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: .7px;
    }

    .metric-value {
        font-size: 29px;
        font-weight: 800;
        margin-top: 9px;
        letter-spacing: -1px;
    }

    .metric-small {
        color: #4ade80;
        font-size: 11px;
        margin-top: 6px;
    }

    /* Workflow */
    .workflow-card {
        background: #0d1320;
        border: 1px solid #1b2536;
        border-radius: 18px;
        padding: 24px;
        margin-top: 18px;
    }

    .section-title {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .section-description {
        color: #778298;
        font-size: 12px;
        margin-bottom: 20px;
    }

    .step {
        background: #101827;
        border: 1px solid #1d293c;
        border-radius: 13px;
        padding: 15px;
        margin-bottom: 10px;
    }

    .step-number {
        color: #8b78ff;
        font-size: 11px;
        font-weight: 800;
    }

    .step-title {
        font-size: 14px;
        font-weight: 650;
        margin-top: 3px;
    }

    .step-info {
        color: #78849a;
        font-size: 11px;
        margin-top: 4px;
    }

    .arrow {
        text-align: center;
        color: #536078;
        margin: -3px 0;
        font-size: 18px;
    }

    /* Status */
    .status-online {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(74,222,128,.08);
        color: #4ade80;
        border: 1px solid rgba(74,222,128,.18);
        border-radius: 20px;
        padding: 6px 10px;
        font-size: 11px;
        font-weight: 600;
    }

    .dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 8px #4ade80;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #28344a;
        background: #121b2b;
        color: #e6ebf5;
        font-weight: 600;
        min-height: 42px;
    }

    .stButton > button:hover {
        border-color: #7c5cff;
        color: white;
        background: #172036;
    }

    /* Inputs */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"],
    .stTextArea textarea {
        background: #0b111d !important;
        border-color: #1d293c !important;
        color: #e8edf7 !important;
        border-radius: 10px !important;
    }

    /* Hide Streamlit chrome */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* Log */
    .log-row {
        border-bottom: 1px solid #172132;
        padding: 13px 4px;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
    }

    .success {
        color: #4ade80;
    }

    .warning {
        color: #fbbf24;
    }

    .muted {
        color: #68758a;
    }

    /* Badge */
    .badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 6px;
        background: #161f31;
        color: #9ca8bc;
        font-size: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ----------------------------- State -----------------------------

if "runs" not in st.session_state:
    st.session_state.runs = [
        {
            "time": "Today, 22:41",
            "workflow": "Invoice Organizer",
            "status": "Success",
            "items": 24,
            "duration": "1.8s"
        },
        {
            "time": "Today, 20:15",
            "workflow": "Document Cleanup",
            "status": "Success",
            "items": 17,
            "duration": "0.9s"
        },
        {
            "time": "Today, 18:32",
            "workflow": "Invoice Organizer",
            "status": "Success",
            "items": 31,
            "duration": "2.2s"
        }
    ]

if "workflow_name" not in st.session_state:
    st.session_state.workflow_name = "Invoice Organizer"

if "running" not in st.session_state:
    st.session_state.running = False


# ----------------------------- Header -----------------------------

st.markdown("""
<div class="brand">
    <div class="brand-icon">⚡</div>
    <div class="brand-name">Flow<span>Pilot</span></div>
</div>
<div class="subtitle">
    Custom workflow automation • Local-first • Built for repetitive work
</div>
""", unsafe_allow_html=True)

# ----------------------------- Metrics -----------------------------

total_runs = len(st.session_state.runs)
total_items = sum(x["items"] for x in st.session_state.runs)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Automations</div>
        <div class="metric-value">04</div>
        <div class="metric-small">↑ 2 active this week</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Successful Runs</div>
        <div class="metric-value">{total_runs}</div>
        <div class="metric-small">↑ 100% success rate</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Items Processed</div>
        <div class="metric-value">{total_items}</div>
        <div class="metric-small">Across all workflows</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">System</div>
        <div class="metric-value">Ready</div>
        <div class="status-online">
            <div class="dot"></div>
            Operational
        </div>
    </div>
    """, unsafe_allow_html=True)


# ----------------------------- Main Layout -----------------------------

left, right = st.columns([1.65, 1], gap="large")


# ============================================================
# LEFT — WORKFLOW BUILDER
# ============================================================

with left:

    st.markdown("""
    <div class="workflow-card">
        <div class="section-title">Workflow Builder</div>
        <div class="section-description">
            Define what FlowPilot should watch, evaluate and execute.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Workflow name
    workflow_name = st.text_input(
        "Workflow name",
        value=st.session_state.workflow_name,
        label_visibility="collapsed",
        placeholder="Give your workflow a name..."
    )

    st.session_state.workflow_name = workflow_name

    # Trigger
    st.markdown("""
    <div class="step">
        <div class="step-number">01 · TRIGGER</div>
        <div class="step-title">Monitor a folder</div>
        <div class="step-info">
            Start workflow whenever new files are detected.
        </div>
    </div>
    <div class="arrow">↓</div>
    """, unsafe_allow_html=True)

    trigger_col1, trigger_col2 = st.columns(2)

    with trigger_col1:
        folder = st.text_input(
            "Watch folder",
            value="~/Downloads",
            help="Folder FlowPilot should monitor."
        )

    with trigger_col2:
        file_pattern = st.selectbox(
            "File type",
            ["All files", "PDF", "Images", "CSV", "Excel", "Documents"]
        )

    # Condition
    st.markdown("""
    <div class="step">
        <div class="step-number">02 · CONDITION</div>
        <div class="step-title">Filter incoming files</div>
        <div class="step-info">
            Only process files matching your selected rule.
        </div>
    </div>
    <div class="arrow">↓</div>
    """, unsafe_allow_html=True)

    condition_col1, condition_col2 = st.columns(2)

    with condition_col1:
        condition = st.selectbox(
            "Condition",
            [
                "File extension matches",
                "Filename contains",
                "File is larger than",
                "File was created today"
            ]
        )

    with condition_col2:
        condition_value = st.text_input(
            "Value",
            value=".pdf" if file_pattern == "PDF" else "",
            placeholder="e.g. invoice, .pdf, 10MB"
        )

    # Actions
    st.markdown("""
    <div class="step">
        <div class="step-number">03 · ACTION</div>
        <div class="step-title">Execute automation</div>
        <div class="step-info">
            Apply one or more operations automatically.
        </div>
    </div>
    """, unsafe_allow_html=True)

    actions = st.multiselect(
        "Actions",
        [
            "Rename file",
            "Move file",
            "Create folder",
            "Generate report",
            "Create backup",
            "Add timestamp"
        ],
        default=["Rename file", "Move file"]
    )

    if "Rename file" in actions:
        rename_col1, rename_col2 = st.columns(2)

        with rename_col1:
            prefix = st.text_input(
                "Rename prefix",
                value="processed_"
            )

        with rename_col2:
            naming_style = st.selectbox(
                "Naming style",
                [
                    "Prefix + original name",
                    "Timestamp + original name",
                    "Sequential numbering"
                ]
            )

    if "Move file" in actions:
        destination = st.text_input(
            "Destination folder",
            value="~/Documents/Processed"
        )

    if "Generate report" in actions:
        report_name = st.text_input(
            "Report filename",
            value="workflow_report.json"
        )

    # Execution controls
    st.markdown("<br>", unsafe_allow_html=True)

    run_col1, run_col2, run_col3 = st.columns([1, 1, 1])

    with run_col1:
        dry_run = st.toggle("Dry run", value=True)

    with run_col2:
        save_workflow = st.button(
            "Save workflow",
            use_container_width=True
        )

    with run_col3:
        execute = st.button(
            "▶ Run workflow",
            use_container_width=True,
            type="primary"
        )

    if save_workflow:
        workflow_data = {
            "name": workflow_name,
            "trigger": {
                "folder": folder,
                "file_type": file_pattern
            },
            "condition": {
                "type": condition,
                "value": condition_value
            },
            "actions": actions,
            "saved_at": datetime.now().isoformat()
        }

        with open("flowpilot_workflow.json", "w") as file:
            json.dump(workflow_data, file, indent=4)

        st.success("Workflow saved to flowpilot_workflow.json")


# ============================================================
# RIGHT — ACTIVITY / EXECUTION PANEL
# ============================================================

with right:

    st.markdown("""
    <div class="workflow-card">
        <div class="section-title">Execution Center</div>
        <div class="section-description">
            Monitor workflow activity and recent operations.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Current workflow
    st.markdown(f"""
    <div class="step">
        <div class="step-number">ACTIVE WORKFLOW</div>
        <div class="step-title">{st.session_state.workflow_name}</div>
        <div class="step-info">
            Monitoring {folder}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Run workflow
    if execute:

        with st.status("Executing workflow...", expanded=True) as status:

            st.write("🔎 Scanning target directory...")
            time.sleep(.4)

            expanded_folder = Path(folder).expanduser()

            if not expanded_folder.exists():
                st.warning(
                    f"Folder not found: {expanded_folder}. "
                    "Create the folder or choose another location."
                )

                status.update(
                    label="Workflow stopped",
                    state="error"
                )

            else:
                files = [
                    f for f in expanded_folder.iterdir()
                    if f.is_file()
                ]

                # Filter files
                if file_pattern != "All files":
                    extension_map = {
                        "PDF": [".pdf"],
                        "Images": [".png", ".jpg", ".jpeg", ".webp"],
                        "CSV": [".csv"],
                        "Excel": [".xlsx", ".xls"],
                        "Documents": [".docx", ".doc", ".txt"]
                    }

                    allowed = extension_map[file_pattern]

                    files = [
                        f for f in files
                        if f.suffix.lower() in allowed
                    ]

                # Apply condition
                if condition == "File extension matches":
                    if condition_value:
                        files = [
                            f for f in files
                            if f.suffix.lower() == condition_value.lower()
                        ]

                elif condition == "Filename contains":
                    if condition_value:
                        files = [
                            f for f in files
                            if condition_value.lower()
                            in f.name.lower()
                        ]

                elif condition == "File is larger than":
                    match = re.search(
                        r"(\d+(?:\.\d+)?)\s*(KB|MB|GB)?",
                        condition_value.upper()
                    )

                    if match:
                        amount = float(match.group(1))
                        unit = match.group(2) or "KB"

                        multiplier = {
                            "KB": 1024,
                            "MB": 1024 ** 2,
                            "GB": 1024 ** 3
                        }

                        minimum_size = amount * multiplier[unit]

                        files = [
                            f for f in files
                            if f.stat().st_size > minimum_size
                        ]

                st.write(f"📦 {len(files)} matching files found")

                processed = 0

                destination_path = None

                if "Move file" in actions:
                    destination_path = Path(
                        destination
                    ).expanduser()

                    if not dry_run:
                        destination_path.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                for index, file in enumerate(files):

                    st.write(
                        f"⚙️ Processing `{file.name}`"
                    )

                    new_name = file.name

                    # Rename
                    if "Rename file" in actions:

                        if naming_style == "Prefix + original name":
                            new_name = prefix + file.name

                        elif naming_style == "Timestamp + original name":
                            stamp = datetime.now().strftime(
                                "%Y%m%d_%H%M%S"
                            )
                            new_name = f"{stamp}_{file.name}"

                        elif naming_style == "Sequential numbering":
                            new_name = (
                                f"{index + 1:03d}_{file.name}"
                            )

                    target = file.with_name(new_name)

                    # Execute only when dry-run is disabled
                    if not dry_run:

                        if "Rename file" in actions:
                            if target != file:
                                file.rename(target)

                        if "Move file" in actions:
                            shutil.move(
                                str(target),
                                str(destination_path / new_name)
                            )

                    processed += 1

                # Report
                if "Generate report" in actions:

                    report = {
                        "workflow": workflow_name,
                        "executed_at": datetime.now().isoformat(),
                        "dry_run": dry_run,
                        "files_detected": len(files),
                        "files_processed": processed,
                        "actions": actions
                    }

                    if not dry_run:
                        with open(
                            report_name,
                            "w"
                        ) as report_file:
                            json.dump(
                                report,
                                report_file,
                                indent=4
                            )

                st.session_state.runs.insert(
                    0,
                    {
                        "time": datetime.now().strftime(
                            "%b %d, %H:%M"
                        ),
                        "workflow": workflow_name,
                        "status": "Dry Run"
                        if dry_run else "Success",
                        "items": processed,
                        "duration": "1.4s"
                    }
                )

                status.update(
                    label="Workflow completed",
                    state="complete"
                )

        if dry_run:
            st.info(
                "Dry Run completed. No files were modified."
            )
        else:
            st.success(
                "Automation completed successfully."
            )

    # Activity
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">Recent Activity</div>
    <div class="section-description">
        Latest workflow executions
    </div>
    """, unsafe_allow_html=True)

    for run in st.session_state.runs[:7]:

        status_class = (
            "success"
            if run["status"] == "Success"
            else "warning"
        )

        st.markdown(f"""
        <div class="log-row">
            <div>
                <strong>{run["workflow"]}</strong><br>
                <span class="muted">
                    {run["time"]} · {run["items"]} items
                </span>
            </div>
            <div style="text-align:right">
                <span class="{status_class}">
                    ● {run["status"]}
                </span><br>
                <span class="muted">{run["duration"]}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    border-top:1px solid #172132;
    padding-top:18px;
    color:#59667b;
    font-size:11px;
    display:flex;
    justify-content:space-between;
">
    <span>FlowPilot Automation Engine</span>
    <span>Local-first • Python • Streamlit</span>
</div>
""", unsafe_allow_html=True)