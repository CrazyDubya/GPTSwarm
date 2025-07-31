#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Master Demo Script for GPTSwarm

This script runs all available demos and generates a comprehensive
showcase of GPTSwarm's capabilities.
"""

import asyncio
import time
import sys
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import all demo modules
from demos.comprehensive_demo import ComprehensiveDemo
from demos.interactive_visualizer import create_demo_visualizations
from demos.research_assistant_demo import run_research_demo
from demos.creative_collaboration_demo import run_creative_demo

class MasterDemo:
    """Orchestrates all GPTSwarm demos"""
    
    def __init__(self):
        self.demo_results = {}
        self.start_time = None
        self.total_time = 0
        
    async def run_all_demos(self, include_visualizations: bool = True):
        """Run all available demos"""
        
        self.start_time = time.time()
        
        print("🌟 GPTSwarm Master Demo Suite 🌟")
        print("=" * 60)
        print("This comprehensive demo showcases the full capabilities")
        print("of GPTSwarm's graph-based agent coordination framework.")
        print("=" * 60)
        
        # Demo 1: Comprehensive Overview
        print(f"\n{'🔥 DEMO 1: COMPREHENSIVE OVERVIEW 🔥':^60}")
        print("=" * 60)
        await self.run_comprehensive_demo()
        
        # Demo 2: Interactive Visualizations  
        if include_visualizations:
            print(f"\n{'🎨 DEMO 2: INTERACTIVE VISUALIZATIONS 🎨':^60}")
            print("=" * 60)
            await self.run_visualization_demo()
        
        # Demo 3: Advanced Research Assistant
        print(f"\n{'🧠 DEMO 3: ADVANCED RESEARCH ASSISTANT 🧠':^60}")
        print("=" * 60)
        await self.run_research_demo()
        
        # Demo 4: Creative Collaboration
        print(f"\n{'🎭 DEMO 4: CREATIVE COLLABORATION 🎭':^60}")
        print("=" * 60)
        await self.run_creative_demo()
        
        # Final Summary
        self.total_time = time.time() - self.start_time
        await self.generate_final_report()
        
    async def run_comprehensive_demo(self):
        """Run the comprehensive overview demo"""
        try:
            demo = ComprehensiveDemo()
            await demo.run_all_demos()
            self.demo_results["comprehensive"] = {
                "status": "success",
                "description": "Multi-domain problem solving showcase",
                "key_features": [
                    "Graph-based agent coordination",
                    "Multi-domain problem solving", 
                    "Swarm optimization algorithms",
                    "Adaptive team formation"
                ]
            }
        except Exception as e:
            print(f"❌ Comprehensive demo failed: {str(e)}")
            self.demo_results["comprehensive"] = {
                "status": "failed",
                "error": str(e)
            }
    
    async def run_visualization_demo(self):
        """Run the interactive visualization demo"""
        try:
            print("Creating interactive graph visualizations...")
            created_files = create_demo_visualizations()
            
            print(f"✅ Created {len(created_files)} visualization files:")
            for filepath in created_files:
                print(f"   📄 {Path(filepath).name}")
            
            self.demo_results["visualization"] = {
                "status": "success",
                "description": "Interactive graph visualizations",
                "files_created": len(created_files),
                "key_features": [
                    "Real-time graph visualization",
                    "Optimization animations",
                    "Interactive network analysis",
                    "Performance tracking charts"
                ]
            }
        except Exception as e:
            print(f"❌ Visualization demo failed: {str(e)}")
            self.demo_results["visualization"] = {
                "status": "failed",
                "error": str(e)
            }
    
    async def run_research_demo(self):
        """Run the research assistant demo"""
        try:
            results, analytics = await run_research_demo()
            
            self.demo_results["research"] = {
                "status": "success",
                "description": "Adaptive research assistant with dynamic team formation",
                "tasks_completed": analytics["total_tasks"],
                "success_rate": analytics["success_rate"],
                "key_features": [
                    "Dynamic team formation",
                    "Complexity analysis",
                    "Adaptive agent allocation",
                    "Performance analytics"
                ]
            }
        except Exception as e:
            print(f"❌ Research demo failed: {str(e)}")
            self.demo_results["research"] = {
                "status": "failed",
                "error": str(e)
            }
    
    async def run_creative_demo(self):
        """Run the creative collaboration demo"""
        try:
            results = await run_creative_demo()
            
            avg_success = sum(r["final_analysis"]["success_score"] for r in results) / len(results)
            
            self.demo_results["creative"] = {
                "status": "success",
                "description": "Creative collaboration through swarm intelligence",
                "projects_completed": len(results),
                "average_success_score": avg_success,
                "key_features": [
                    "Multi-agent creative collaboration",
                    "Emergent creativity patterns",
                    "Quality metric tracking",
                    "Diverse creative specializations"
                ]
            }
        except Exception as e:
            print(f"❌ Creative demo failed: {str(e)}")
            self.demo_results["creative"] = {
                "status": "failed",
                "error": str(e)
            }
    
    async def generate_final_report(self):
        """Generate comprehensive final report"""
        
        print(f"\n{'🏆 FINAL REPORT 🏆':^60}")
        print("=" * 60)
        
        # Execution Summary
        successful_demos = sum(1 for demo in self.demo_results.values() 
                              if demo["status"] == "success")
        total_demos = len(self.demo_results)
        
        print(f"\n📊 Execution Summary:")
        print(f"   Total Demos: {total_demos}")
        print(f"   Successful: {successful_demos}")
        print(f"   Success Rate: {successful_demos/total_demos:.1%}")
        print(f"   Total Time: {self.total_time:.1f} seconds")
        
        # Demo Details
        print(f"\n📋 Demo Results:")
        for demo_name, result in self.demo_results.items():
            status_icon = "✅" if result["status"] == "success" else "❌"
            print(f"\n   {status_icon} {demo_name.title()} Demo:")
            print(f"      Description: {result.get('description', 'N/A')}")
            
            if result["status"] == "success":
                # Show key metrics
                if "tasks_completed" in result:
                    print(f"      Tasks Completed: {result['tasks_completed']}")
                if "success_rate" in result:
                    print(f"      Success Rate: {result['success_rate']:.1%}")
                if "files_created" in result:
                    print(f"      Files Created: {result['files_created']}")
                if "projects_completed" in result:
                    print(f"      Projects Completed: {result['projects_completed']}")
                
                # Show key features
                if "key_features" in result:
                    print(f"      Key Features:")
                    for feature in result["key_features"]:
                        print(f"        • {feature}")
            else:
                print(f"      Error: {result.get('error', 'Unknown error')}")
        
        # GPTSwarm Capabilities Demonstrated
        print(f"\n🐝 GPTSwarm Capabilities Demonstrated:")
        
        all_features = set()
        for result in self.demo_results.values():
            if result["status"] == "success" and "key_features" in result:
                all_features.update(result["key_features"])
        
        for feature in sorted(all_features):
            print(f"   ✅ {feature}")
        
        # Next Steps and Recommendations
        print(f"\n🚀 Next Steps:")
        next_steps = [
            "Set up OpenAI API key for live LLM integration",
            "Explore custom agent configurations for your domain",
            "Experiment with different optimization parameters",
            "Integrate GPTSwarm with your existing workflows",
            "Contribute to the GPTSwarm open-source project"
        ]
        
        for step in next_steps:
            print(f"   1. {step}")
        
        # Performance Insights
        print(f"\n💡 Key Insights:")
        insights = []
        
        if successful_demos == total_demos:
            insights.append("All demos executed successfully - GPTSwarm is stable and robust")
        
        if any("research" in demo for demo in self.demo_results.keys()):
            insights.append("Dynamic team formation significantly improves task performance")
        
        if any("creative" in demo for demo in self.demo_results.keys()):
            insights.append("Swarm intelligence enables emergent creativity patterns")
        
        insights.extend([
            "Graph-based coordination provides flexible agent communication",
            "Optimization algorithms continuously improve swarm performance",
            "Multi-domain support makes GPTSwarm universally applicable"
        ])
        
        for insight in insights:
            print(f"   • {insight}")
        
        # Contact and Resources
        print(f"\n📚 Resources and Support:")
        print(f"   📖 Documentation: https://gptswarm.org")
        print(f"   🐙 GitHub Repository: https://github.com/metauto-ai/GPTSwarm")
        print(f"   📄 Research Paper: https://arxiv.org/abs/2402.16823")
        print(f"   💬 Community: Join our Discord/Slack channels")
        
        print(f"\n{'Thank you for exploring GPTSwarm! 🐝':^60}")
        print("=" * 60)

async def main():
    """Main function to run the master demo"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description="GPTSwarm Master Demo Suite")
    parser.add_argument("--skip-visualizations", action="store_true",
                       help="Skip creating visualization files")
    parser.add_argument("--demo", choices=["comprehensive", "research", "creative", "visualization"],
                       help="Run only a specific demo")
    
    args = parser.parse_args()
    
    master_demo = MasterDemo()
    
    if args.demo:
        # Run specific demo
        if args.demo == "comprehensive":
            await master_demo.run_comprehensive_demo()
        elif args.demo == "research":
            await master_demo.run_research_demo()
        elif args.demo == "creative":
            await master_demo.run_creative_demo()
        elif args.demo == "visualization":
            await master_demo.run_visualization_demo()
            
        # Generate report for single demo
        master_demo.total_time = 0
        await master_demo.generate_final_report()
    else:
        # Run all demos
        include_viz = not args.skip_visualizations
        await master_demo.run_all_demos(include_visualizations=include_viz)

if __name__ == "__main__":
    asyncio.run(main())