# GPTSwarm Demo Troubleshooting Guide

This guide helps resolve common issues when running the GPTSwarm demos.

## Common Issues and Solutions

### 1. Import Errors

**Error**: `ModuleNotFoundError: No module named 'swarm'`

**Solution**:
```bash
# Make sure you're in the right directory
cd GPTSwarm

# Run demos from the project root
python demos/comprehensive_demo.py

# Or set PYTHONPATH explicitly
PYTHONPATH=. python demos/comprehensive_demo.py
```

### 2. Missing Dependencies

**Error**: `ModuleNotFoundError: No module named 'shortuuid'`

**Solutions**:
1. **With network access**:
   ```bash
   pip install shortuuid networkx loguru
   # Or install full dependencies
   pip install -e .
   ```

2. **Without network access**:
   The demos include mock implementations and should work with minimal dependencies. If you see import errors, comment out problematic imports in the demo files.

### 3. OpenAI API Issues

**Error**: `AuthenticationError` or `RateLimitError`

**Solutions**:
1. **Use mock mode** (default in demos):
   ```python
   demo = ComprehensiveDemo()
   demo.use_mock = True  # This is already the default
   ```

2. **For real API usage**:
   ```bash
   # Set your API key
   export OPENAI_API_KEY="your-api-key-here"
   ```

### 4. Visualization Files Not Created

**Error**: HTML files not generated in `demos/visualizations/`

**Solutions**:
1. **Check directory permissions**:
   ```bash
   mkdir -p demos/visualizations
   chmod 755 demos/visualizations
   ```

2. **Run visualizer separately**:
   ```bash
   python demos/interactive_visualizer.py
   ```

### 5. Performance Issues

**Symptom**: Demos running slowly

**Solutions**:
1. **Reduce iteration counts**:
   ```python
   # In the demo files, reduce max_iterations
   await demo.run_creative_session(project, max_iterations=2)  # Instead of 5
   ```

2. **Skip heavy demos**:
   ```bash
   # Run only specific demos
   python demos/master_demo.py --demo comprehensive
   python demos/master_demo.py --skip-visualizations
   ```

### 6. Memory Issues

**Error**: `MemoryError` or system slow down

**Solutions**:
1. **Reduce team sizes**:
   ```python
   # In research_assistant_demo.py
   team = swarm.form_creative_team(project_type, team_size=2)  # Instead of 4
   ```

2. **Run demos individually**:
   ```bash
   # Instead of master_demo.py, run one at a time
   python demos/comprehensive_demo.py
   ```

## Environment Setup

### Minimal Environment
For basic demo functionality:
```bash
# Required Python version
python --version  # Should be 3.8+

# Minimal dependencies (if needed)
pip install asyncio  # Usually built-in
```

### Full Environment
For complete functionality:
```bash
# Clone repository
git clone https://github.com/metauto-ai/GPTSwarm.git
cd GPTSwarm

# Install with conda (recommended)
conda create -n gptswarm python=3.10
conda activate gptswarm
pip install -e .

# Or with pip
pip install -e .
```

## Configuration Tips

### 1. Customize Demo Behavior

```python
# In any demo file, you can adjust:

# Execution speed
await asyncio.sleep(0.01)  # Faster execution

# Team sizes
team_size = 2  # Smaller teams

# Iteration counts
max_iterations = 2  # Fewer iterations

# Mock responses
use_mock = True  # Always use mock
```

### 2. Debug Mode

Add debug output to any demo:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Add debug prints
print(f"DEBUG: Current state = {current_state}")
```

### 3. Output Customization

```python
# Reduce output verbosity
verbose = False
if verbose:
    print("Detailed output...")

# Save results to file
import json
with open('demo_results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

## Platform-Specific Issues

### Windows
- Use `python` instead of `python3`
- Path separators: use `Path` from `pathlib` for cross-platform compatibility
- PowerShell: Set execution policy if needed

### macOS
- May need to install Xcode command line tools
- Use `python3` explicitly if multiple Python versions

### Linux
- Usually works out of the box
- Check Python version with `python3 --version`

## Getting Help

If you encounter issues not covered here:

1. **Check the main README**: [`../README.md`](../README.md)
2. **Open an issue**: [GitHub Issues](https://github.com/metauto-ai/GPTSwarm/issues)
3. **Check documentation**: [GPTSwarm Documentation](https://gptswarm.org)
4. **Community support**: Join our Discord/Slack channels

## Contributing Fixes

Found a bug or have a fix? Please contribute:

1. Fork the repository
2. Create a fix in your branch
3. Test thoroughly with the demos
4. Submit a pull request

---

**Happy debugging! 🐛➡️🐝**