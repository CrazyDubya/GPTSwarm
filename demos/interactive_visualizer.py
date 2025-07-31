#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interactive Graph Visualization Demo for GPTSwarm

This demo creates interactive HTML visualizations of agent graphs,
showing how agents connect and optimize their relationships over time.
"""

import json
import os
from typing import Dict, List, Any, Tuple
from pathlib import Path

class GraphVisualizer:
    """Creates interactive visualizations of GPTSwarm agent graphs"""
    
    def __init__(self, output_dir: str = "demos/visualizations"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def create_interactive_graph(self, 
                                config: Dict[str, Any], 
                                optimization_data: List[float] = None) -> str:
        """Create an interactive HTML graph visualization"""
        
        graph_data = self._generate_graph_data(config)
        html_content = self._generate_html_visualization(config, graph_data, optimization_data)
        
        filename = f"graph_{config['name'].lower().replace(' ', '_')}.html"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w') as f:
            f.write(html_content)
            
        return str(filepath)
    
    def _generate_graph_data(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Generate graph structure data"""
        agents = config["agents"]
        num_agents = len(agents)
        
        # Create nodes
        nodes = []
        for i, agent_type in enumerate(agents):
            nodes.append({
                "id": i,
                "label": f"{agent_type}_{i}",
                "type": agent_type,
                "color": self._get_agent_color(agent_type),
                "size": 20 if agent_type == "TOT" else 15
            })
        
        # Create edges based on connection pattern
        edges = []
        edge_id = 0
        
        if config["connections"] == "sequential":
            for i in range(num_agents - 1):
                edges.append({
                    "id": edge_id,
                    "from": i,
                    "to": i + 1,
                    "weight": 0.8,
                    "color": "#2E8B57"
                })
                edge_id += 1
                
        elif config["connections"] == "full":
            for i in range(num_agents):
                for j in range(i + 1, num_agents):
                    edges.append({
                        "id": edge_id,
                        "from": i,
                        "to": j,
                        "weight": 0.6,
                        "color": "#4169E1"
                    })
                    edge_id += 1
                    
        elif config["connections"] == "hub":
            hub_node = 0  # First node is the hub
            for i in range(1, num_agents):
                edges.append({
                    "id": edge_id,
                    "from": hub_node,
                    "to": i,
                    "weight": 0.7,
                    "color": "#DC143C"
                })
                edge_id += 1
        
        return {
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "num_nodes": num_agents,
                "num_edges": len(edges),
                "connectivity": len(edges) / (num_agents * (num_agents - 1) / 2) if num_agents > 1 else 0
            }
        }
    
    def _get_agent_color(self, agent_type: str) -> str:
        """Get color for different agent types"""
        colors = {
            "IO": "#FF6B6B",
            "TOT": "#4ECDC4",
            "COT": "#45B7D1",
            "WEB": "#96CEB4",
            "TOOL": "#FFEAA7"
        }
        return colors.get(agent_type, "#DDA0DD")
    
    def _generate_html_visualization(self, 
                                   config: Dict[str, Any], 
                                   graph_data: Dict[str, Any],
                                   optimization_data: List[float] = None) -> str:
        """Generate the complete HTML visualization"""
        
        nodes_json = json.dumps(graph_data["nodes"])
        edges_json = json.dumps(graph_data["edges"])
        optimization_json = json.dumps(optimization_data or [])
        
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>GPTSwarm: {config['name']} Configuration</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            backdrop-filter: blur(10px);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        .header p {{
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .graph-container {{
            background: white;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        .graph-canvas {{
            width: 100%;
            height: 500px;
            border-radius: 10px;
        }}
        .stats-panel {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            backdrop-filter: blur(5px);
        }}
        .stat-value {{
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }}
        .legend {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 20px 0;
            flex-wrap: wrap;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .legend-color {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
        }}
        .optimization-panel {{
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        #optimization-chart {{
            background: white;
            border-radius: 5px;
            margin: 10px 0;
        }}
        .controls {{
            text-align: center;
            margin: 20px 0;
        }}
        .btn {{
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            margin: 0 10px;
            transition: all 0.3s ease;
        }}
        .btn:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }}
    </style>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐝 GPTSwarm Visualization</h1>
            <p>{config['name']} Configuration</p>
            <p>{config['description']}</p>
        </div>
        
        <div class="stats-panel">
            <div class="stat-card">
                <div>Agent Count</div>
                <div class="stat-value">{graph_data['stats']['num_nodes']}</div>
            </div>
            <div class="stat-card">
                <div>Connections</div>
                <div class="stat-value">{graph_data['stats']['num_edges']}</div>
            </div>
            <div class="stat-card">
                <div>Connectivity</div>
                <div class="stat-value">{graph_data['stats']['connectivity']:.1%}</div>
            </div>
        </div>
        
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color" style="background: #FF6B6B;"></div>
                <span>IO Agent</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #4ECDC4;"></div>
                <span>TOT Agent</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #45B7D1;"></div>
                <span>COT Agent</span>
            </div>
        </div>
        
        <div class="graph-container">
            <div id="graph-canvas" class="graph-canvas"></div>
        </div>
        
        <div class="controls">
            <button class="btn" onclick="resetGraph()">Reset View</button>
            <button class="btn" onclick="animateGraph()">Animate</button>
            <button class="btn" onclick="showOptimization()">Show Optimization</button>
        </div>
        
        <div class="optimization-panel" id="optimization-panel" style="display: none;">
            <h3>🚀 Optimization Progress</h3>
            <div id="optimization-chart" style="height: 300px;"></div>
        </div>
    </div>

    <script>
        // Graph data
        const nodes = new vis.DataSet({nodes_json});
        const edges = new vis.DataSet({edges_json});
        const optimizationData = {optimization_json};
        
        // Graph options
        const options = {{
            nodes: {{
                borderWidth: 2,
                borderColor: '#ffffff',
                font: {{
                    color: '#333333',
                    size: 12,
                    face: 'arial'
                }},
                shadow: {{
                    enabled: true,
                    color: 'rgba(0,0,0,0.2)',
                    size: 10,
                    x: 2,
                    y: 2
                }}
            }},
            edges: {{
                width: 3,
                shadow: {{
                    enabled: true,
                    color: 'rgba(0,0,0,0.1)',
                    size: 5,
                    x: 1,
                    y: 1
                }},
                smooth: {{
                    type: 'continuous',
                    roundness: 0.2
                }}
            }},
            physics: {{
                enabled: true,
                stabilization: {{
                    enabled: true,
                    iterations: 1000,
                    updateInterval: 25
                }},
                barnesHut: {{
                    gravitationalConstant: -8000,
                    centralGravity: 0.3,
                    springLength: 95,
                    springConstant: 0.04,
                    damping: 0.09
                }}
            }},
            interaction: {{
                hover: true,
                tooltipDelay: 200
            }}
        }};
        
        // Create network
        const container = document.getElementById('graph-canvas');
        const data = {{ nodes: nodes, edges: edges }};
        const network = new vis.Network(container, data, options);
        
        // Add hover effects
        network.on('hoverNode', function(params) {{
            const nodeId = params.node;
            const connectedEdges = network.getConnectedEdges(nodeId);
            const connectedNodes = network.getConnectedNodes(nodeId);
            
            // Highlight connected elements
            edges.update(connectedEdges.map(edgeId => ({{
                id: edgeId,
                color: {{ color: '#FFD700', opacity: 1 }}
            }})));
        }});
        
        network.on('blurNode', function(params) {{
            // Reset edge colors
            edges.forEach(edge => {{
                edges.update({{
                    id: edge.id,
                    color: edge.color
                }});
            }});
        }});
        
        // Control functions
        function resetGraph() {{
            network.fit();
        }}
        
        function animateGraph() {{
            const nodeIds = nodes.getIds();
            let index = 0;
            
            function highlightNext() {{
                // Reset all nodes
                nodes.forEach(node => {{
                    nodes.update({{
                        id: node.id,
                        color: node.color,
                        size: node.size
                    }});
                }});
                
                // Highlight current node
                const currentNode = nodeIds[index];
                nodes.update({{
                    id: currentNode,
                    size: 30,
                    color: '#FFD700'
                }});
                
                index = (index + 1) % nodeIds.length;
                setTimeout(highlightNext, 1000);
            }}
            
            highlightNext();
        }}
        
        function showOptimization() {{
            const panel = document.getElementById('optimization-panel');
            panel.style.display = panel.style.display === 'none' ? 'block' : 'none';
            
            if (panel.style.display === 'block' && optimizationData.length > 0) {{
                plotOptimization();
            }}
        }}
        
        function plotOptimization() {{
            const trace = {{
                x: optimizationData.map((_, i) => i),
                y: optimizationData,
                type: 'scatter',
                mode: 'lines+markers',
                line: {{
                    color: '#667eea',
                    width: 3
                }},
                marker: {{
                    color: '#764ba2',
                    size: 8
                }},
                name: 'Performance'
            }};
            
            const layout = {{
                title: 'Swarm Optimization Progress',
                xaxis: {{
                    title: 'Iteration'
                }},
                yaxis: {{
                    title: 'Performance Score',
                    tickformat: '.1%'
                }},
                margin: {{ t: 50, r: 50, b: 50, l: 70 }}
            }};
            
            Plotly.newPlot('optimization-chart', [trace], layout);
        }}
        
        // Initialize
        network.once('stabilizationIterationsDone', function() {{
            network.setOptions({{ physics: false }});
        }});
    </script>
</body>
</html>
"""
        return html_template
    
    def create_optimization_animation(self, 
                                    config: Dict[str, Any],
                                    optimization_steps: List[Dict[str, Any]]) -> str:
        """Create an animated visualization of the optimization process"""
        
        filename = f"optimization_{config['name'].lower().replace(' ', '_')}.html"
        filepath = self.output_dir / filename
        
        html_content = self._generate_optimization_html(config, optimization_steps)
        
        with open(filepath, 'w') as f:
            f.write(html_content)
            
        return str(filepath)
    
    def _generate_optimization_html(self, 
                                   config: Dict[str, Any],
                                   optimization_steps: List[Dict[str, Any]]) -> str:
        """Generate HTML for optimization animation"""
        
        steps_json = json.dumps(optimization_steps)
        
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>GPTSwarm Optimization Animation</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .animation-container {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .controls {{
            text-align: center;
            margin: 20px 0;
        }}
        .btn {{
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            margin: 0 10px;
            font-size: 16px;
            transition: all 0.3s ease;
        }}
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        .progress-bar {{
            background: #f0f0f0;
            border-radius: 10px;
            height: 20px;
            margin: 20px 0;
            overflow: hidden;
        }}
        .progress-fill {{
            background: linear-gradient(45deg, #667eea, #764ba2);
            height: 100%;
            transition: width 0.5s ease;
            border-radius: 10px;
        }}
        .step-info {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 10px 0;
        }}
    </style>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 GPTSwarm Optimization Animation</h1>
            <p>Watch how the swarm optimizes its performance over time</p>
        </div>
        
        <div class="animation-container">
            <div id="graph-canvas" style="height: 400px;"></div>
        </div>
        
        <div class="step-info">
            <span>Step: <span id="current-step">0</span> / <span id="total-steps">0</span></span>
            <span>Performance: <span id="current-performance">0%</span></span>
        </div>
        
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 0%;"></div>
        </div>
        
        <div class="controls">
            <button class="btn" onclick="startAnimation()">Start</button>
            <button class="btn" onclick="pauseAnimation()">Pause</button>
            <button class="btn" onclick="resetAnimation()">Reset</button>
            <button class="btn" onclick="stepForward()">Step Forward</button>
        </div>
    </div>

    <script>
        const optimizationSteps = {steps_json};
        let currentStep = 0;
        let animationRunning = false;
        let animationTimer = null;
        
        // Initialize graph
        const container = document.getElementById('graph-canvas');
        let network = null;
        
        function initializeGraph() {{
            const initialStep = optimizationSteps[0] || {{
                nodes: [{{id: 0, label: 'Agent_0', color: '#FF6B6B'}}],
                edges: [],
                performance: 0.5
            }};
            
            const nodes = new vis.DataSet(initialStep.nodes);
            const edges = new vis.DataSet(initialStep.edges);
            
            const options = {{
                nodes: {{
                    borderWidth: 2,
                    borderColor: '#ffffff',
                    font: {{ color: '#333333', size: 12 }},
                    shadow: true
                }},
                edges: {{
                    width: 3,
                    shadow: true,
                    smooth: {{ type: 'continuous' }}
                }},
                physics: {{
                    enabled: true,
                    stabilization: {{ iterations: 100 }}
                }}
            }};
            
            network = new vis.Network(container, {{ nodes, edges }}, options);
            updateStepInfo();
        }}
        
        function updateGraph() {{
            if (currentStep >= optimizationSteps.length) return;
            
            const step = optimizationSteps[currentStep];
            const nodes = new vis.DataSet(step.nodes);
            const edges = new vis.DataSet(step.edges);
            
            network.setData({{ nodes, edges }});
            updateStepInfo();
        }}
        
        function updateStepInfo() {{
            document.getElementById('current-step').textContent = currentStep;
            document.getElementById('total-steps').textContent = optimizationSteps.length - 1;
            
            if (currentStep < optimizationSteps.length) {{
                const performance = optimizationSteps[currentStep].performance;
                document.getElementById('current-performance').textContent = 
                    (performance * 100).toFixed(1) + '%';
                
                const progress = (currentStep / (optimizationSteps.length - 1)) * 100;
                document.getElementById('progress-fill').style.width = progress + '%';
            }}
        }}
        
        function startAnimation() {{
            if (animationRunning) return;
            
            animationRunning = true;
            animationTimer = setInterval(() => {{
                stepForward();
                if (currentStep >= optimizationSteps.length - 1) {{
                    pauseAnimation();
                }}
            }}, 1000);
        }}
        
        function pauseAnimation() {{
            animationRunning = false;
            if (animationTimer) {{
                clearInterval(animationTimer);
                animationTimer = null;
            }}
        }}
        
        function resetAnimation() {{
            pauseAnimation();
            currentStep = 0;
            updateGraph();
        }}
        
        function stepForward() {{
            if (currentStep < optimizationSteps.length - 1) {{
                currentStep++;
                updateGraph();
            }}
        }}
        
        // Initialize
        if (optimizationSteps.length > 0) {{
            initializeGraph();
        }}
    </script>
</body>
</html>
"""
        return html_template

def create_demo_visualizations():
    """Create all demo visualizations"""
    
    visualizer = GraphVisualizer()
    
    # Demo configurations
    configs = [
        {
            "name": "Linear Chain",
            "agents": ["IO", "TOT", "IO"],
            "connections": "sequential",
            "description": "Agents process information sequentially"
        },
        {
            "name": "Fully Connected",
            "agents": ["IO", "IO", "IO", "IO"],
            "connections": "full",
            "description": "All agents can communicate with each other"
        },
        {
            "name": "Hub and Spoke",
            "agents": ["IO", "TOT", "IO", "IO"],
            "connections": "hub",
            "description": "Central agent coordinates with others"
        }
    ]
    
    created_files = []
    
    # Create static visualizations
    for config in configs:
        # Create optimization data
        optimization_data = [0.5 + i * 0.03 + (i * 0.001) for i in range(15)]
        
        filepath = visualizer.create_interactive_graph(config, optimization_data)
        created_files.append(filepath)
        print(f"Created visualization: {filepath}")
    
    # Create optimization animation
    optimization_steps = []
    for i in range(10):
        performance = 0.5 + i * 0.04
        nodes = [
            {"id": j, "label": f"Agent_{j}", "color": "#FF6B6B", "size": 15 + i}
            for j in range(3)
        ]
        edges = [
            {"id": 0, "from": 0, "to": 1, "color": f"hsl({120 + i*10}, 70%, 50%)"},
            {"id": 1, "from": 1, "to": 2, "color": f"hsl({120 + i*10}, 70%, 50%)"}
        ]
        
        optimization_steps.append({
            "nodes": nodes,
            "edges": edges,
            "performance": performance
        })
    
    optimization_file = visualizer.create_optimization_animation(
        {"name": "Edge Optimization"}, optimization_steps
    )
    created_files.append(optimization_file)
    print(f"Created optimization animation: {optimization_file}")
    
    return created_files

if __name__ == "__main__":
    files = create_demo_visualizations()
    print(f"\n🎨 Created {len(files)} visualization files!")
    print("Open these HTML files in your browser to see the interactive demos.")