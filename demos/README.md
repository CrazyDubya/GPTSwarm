# GPTSwarm Comprehensive Demo Suite 🐝

This directory contains a comprehensive set of demos that showcase the full capabilities of GPTSwarm's graph-based agent coordination framework. These demos are designed to illustrate the unique features and advantages of using swarm intelligence for complex problem-solving tasks.

## 🌟 Demo Overview

The demo suite consists of four main demonstrations that highlight different aspects of GPTSwarm:

1. **[Comprehensive Demo](#comprehensive-demo)** - Multi-domain problem solving showcase
2. **[Interactive Visualizations](#interactive-visualizations)** - Real-time graph visualizations
3. **[Advanced Research Assistant](#advanced-research-assistant)** - Dynamic team formation for research tasks
4. **[Creative Collaboration](#creative-collaboration)** - Emergent creativity through swarm intelligence

## 🚀 Quick Start

### Prerequisites

```bash
# Clone the repository
git clone https://github.com/metauto-ai/GPTSwarm.git
cd GPTSwarm

# Install dependencies (if you have network access)
pip install -e .

# Or run demos with minimal dependencies (they include mock implementations)
cd demos
```

### Run All Demos

```bash
# Run the complete demo suite
python master_demo.py

# Run specific demo only
python master_demo.py --demo comprehensive
python master_demo.py --demo research
python master_demo.py --demo creative
python master_demo.py --demo visualization

# Skip visualization files (for faster execution)
python master_demo.py --skip-visualizations
```

### Run Individual Demos

```bash
# Comprehensive overview
python comprehensive_demo.py

# Research assistant
python research_assistant_demo.py

# Creative collaboration
python creative_collaboration_demo.py

# Interactive visualizations
python interactive_visualizer.py
```

## 📊 Demo Descriptions

### Comprehensive Demo

**File:** `comprehensive_demo.py`

A complete overview of GPTSwarm's core capabilities including:

- **Multi-Domain Problem Solving**: Automatically routes different types of problems (math, coding, research) to appropriate agent configurations
- **Agent Graph Visualization**: Shows different graph topologies (linear, fully-connected, hub-and-spoke)
- **Swarm Optimization**: Demonstrates edge and node optimization algorithms
- **Adaptive Research Assistant**: Dynamic team formation based on task complexity
- **Creative Content Generation**: Collaborative content creation with multiple agent perspectives

**Key Features Demonstrated:**
- Graph-based agent coordination
- Multi-domain problem solving
- Swarm optimization algorithms
- Adaptive team formation
- Creative collaboration
- Real-time visualization

### Interactive Visualizations

**File:** `interactive_visualizer.py`

Creates interactive HTML visualizations that show:

- **Static Graph Visualizations**: Different agent network topologies with interactive features
- **Optimization Animations**: Real-time visualization of swarm optimization processes
- **Performance Tracking**: Charts showing performance improvements over time
- **Interactive Controls**: User controls for graph manipulation and animation

**Generated Files:**
- `visualizations/graph_linear_chain.html`
- `visualizations/graph_fully_connected.html`
- `visualizations/graph_hub_and_spoke.html`
- `visualizations/optimization_edge_optimization.html`

**Technologies Used:**
- Vis.js for network visualization
- Plotly.js for charts and graphs
- Custom CSS for beautiful styling
- Responsive design for different screen sizes

### Advanced Research Assistant

**File:** `research_assistant_demo.py`

Demonstrates intelligent research task processing with:

- **Task Complexity Analysis**: Automatically analyzes research queries to determine complexity and required skills
- **Dynamic Team Formation**: Forms optimal agent teams based on task requirements
- **Adaptive Resource Allocation**: Adjusts team size and composition for different complexity levels
- **Performance Analytics**: Tracks success rates across different task types and team configurations

**Research Query Examples:**
- Simple: "What is machine learning?"
- Medium: "Compare renewable energy technologies"
- Complex: "Analyze AI impact on healthcare with case studies"

**Metrics Tracked:**
- Task completion rates
- Performance by complexity level
- Team configuration effectiveness
- Resource utilization efficiency

### Creative Collaboration

**File:** `creative_collaboration_demo.py`

Showcases emergent creativity through multi-agent collaboration:

- **Specialized Creative Agents**: Different agents with specific creative roles (idea generator, story writer, critic, etc.)
- **Collaborative Project Development**: Agents work together on creative projects with iterative improvement
- **Quality Metrics Tracking**: Measures creativity, coherence, originality, and engagement
- **Emergence Analysis**: Studies how collective intelligence produces better creative outcomes

**Project Types:**
- **Story Writing**: Collaborative science fiction narratives
- **Concept Design**: Innovative framework development
- **Problem Solving**: Creative solution brainstorming

**Agent Specializations:**
- Idea Generator
- Story Writer
- Concept Developer
- Critic/Reviewer
- Style Enhancer
- Structure Organizer

## 🎯 Key Features Demonstrated

### Graph-Based Coordination
- Flexible agent communication patterns
- Dynamic topology optimization
- Efficient information flow

### Swarm Intelligence
- Collective problem-solving capabilities
- Emergent behavior patterns
- Self-optimization algorithms

### Adaptive Systems
- Dynamic team formation
- Task-specific agent allocation
- Real-time performance adjustment

### Multi-Domain Support
- Mathematics and reasoning
- Code generation and analysis
- Research and synthesis
- Creative content generation

### Optimization Algorithms
- Edge optimization for connectivity
- Node optimization for performance
- Performance tracking and improvement

## 📈 Demo Results and Metrics

Each demo provides detailed analytics including:

- **Performance Metrics**: Success rates, quality scores, efficiency measures
- **Collaboration Analysis**: Team effectiveness, participation balance, communication patterns
- **Optimization Progress**: Performance improvements over time
- **Comparative Studies**: Different configurations and their relative performance

## 🛠️ Customization and Extension

The demos are designed to be easily customizable:

### Adding New Domains
```python
# In comprehensive_demo.py
new_problems = [
    {
        "type": "your_domain",
        "task": "Your specific task",
        "expected_agents": ["IO", "TOT"]
    }
]
```

### Creating Custom Agents
```python
# In creative_collaboration_demo.py
class CustomCreativeAgent(CreativeAgent):
    def __init__(self, specialization):
        super().__init__("CUSTOM", specialization)
        
    def generate_contribution(self, context, iteration):
        # Your custom contribution logic
        pass
```

### Modifying Visualization Styles
```html
<!-- In interactive_visualizer.py HTML templates -->
<style>
    /* Customize colors, layouts, animations */
    .your-custom-styles {
        /* Your styling */
    }
</style>
```

## 🔧 Configuration Options

### Mock vs Live LLM
```python
# Use mock responses for demo purposes
demo = ComprehensiveDemo()
demo.use_mock = True

# Use real OpenAI API (requires OPENAI_API_KEY)
demo.use_mock = False
```

### Optimization Parameters
```python
# Adjust optimization settings
swarm = Swarm(
    agents=["IO", "TOT"],
    domain="gaia",
    edge_optimize=True,
    node_optimize=True,
    init_connection_probability=0.5
)
```

### Team Formation Strategy
```python
# Customize team formation
team_config = {
    "complexity_threshold": 0.7,
    "max_team_size": 6,
    "specialization_priority": ["research", "analysis", "synthesis"]
}
```

## 📚 Educational Value

These demos serve as:

- **Learning Tools**: Understand graph-based agent systems
- **Research Examples**: See swarm intelligence in action
- **Development Templates**: Starting points for custom applications
- **Performance Benchmarks**: Compare different approaches and configurations

## 🤝 Contributing

To add new demos or improve existing ones:

1. Follow the existing code structure and patterns
2. Include comprehensive documentation and comments
3. Add appropriate error handling and validation
4. Create meaningful examples and test cases
5. Update this README with your additions

## 📄 License

These demos are part of the GPTSwarm project and are released under the MIT License.

## 🔗 Related Resources

- **Main Repository**: [GPTSwarm GitHub](https://github.com/metauto-ai/GPTSwarm)
- **Research Paper**: [Language Agents as Optimizable Graphs](https://arxiv.org/abs/2402.16823)
- **Project Website**: [gptswarm.org](https://gptswarm.org)
- **Documentation**: See main repository documentation

---

**Happy Swarming! 🐝**

*For questions, issues, or contributions, please visit our GitHub repository or join our community discussions.*