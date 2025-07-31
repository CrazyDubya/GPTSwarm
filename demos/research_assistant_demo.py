#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Advanced Research Assistant Demo for GPTSwarm

This demo showcases dynamic agent team formation for complex research tasks,
demonstrating how GPTSwarm can adapt its agent configuration based on task requirements.
"""

import asyncio
import json
import sys
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from datetime import datetime
import random

# Add the swarm module to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

class ResearchTask:
    """Represents a research task with complexity analysis"""
    
    def __init__(self, 
                 query: str, 
                 domain: str = "general",
                 complexity: str = "medium",
                 required_skills: List[str] = None,
                 time_limit: int = 300):
        self.query = query
        self.domain = domain
        self.complexity = complexity
        self.required_skills = required_skills or []
        self.time_limit = time_limit
        self.created_at = datetime.now()
        
    def analyze_complexity(self) -> Dict[str, Any]:
        """Analyze task complexity based on query characteristics"""
        
        complexity_indicators = {
            "high": ["compare", "analyze", "evaluate", "synthesize", "integrate", "comprehensive"],
            "medium": ["explain", "describe", "summarize", "overview", "review"],
            "low": ["what", "when", "where", "who", "define", "list"]
        }
        
        query_lower = self.query.lower()
        
        # Count complexity indicators
        complexity_scores = {}
        for level, indicators in complexity_indicators.items():
            score = sum(1 for indicator in indicators if indicator in query_lower)
            complexity_scores[level] = score
        
        # Determine complexity
        if complexity_scores["high"] > 0:
            complexity = "high"
        elif complexity_scores["medium"] > 0:
            complexity = "medium"
        else:
            complexity = "low"
        
        # Determine required skills
        skills = []
        if any(word in query_lower for word in ["search", "find", "research"]):
            skills.append("research")
        if any(word in query_lower for word in ["analyze", "analysis", "compare"]):
            skills.append("analysis")
        if any(word in query_lower for word in ["code", "program", "algorithm"]):
            skills.append("coding")
        if any(word in query_lower for word in ["synthesize", "combine", "integrate"]):
            skills.append("synthesis")
        if any(word in query_lower for word in ["creative", "design", "innovative"]):
            skills.append("creativity")
        
        return {
            "complexity": complexity,
            "skills": skills,
            "estimated_time": self._estimate_time(complexity),
            "agent_count": self._estimate_agent_count(complexity, skills)
        }
    
    def _estimate_time(self, complexity: str) -> int:
        """Estimate task completion time"""
        time_estimates = {
            "low": 60,     # 1 minute
            "medium": 180,  # 3 minutes
            "high": 600    # 10 minutes
        }
        return time_estimates.get(complexity, 180)
    
    def _estimate_agent_count(self, complexity: str, skills: List[str]) -> int:
        """Estimate required number of agents"""
        base_count = {"low": 2, "medium": 3, "high": 4}
        skill_bonus = len(skills) // 2
        return min(base_count.get(complexity, 3) + skill_bonus, 6)

class AgentTeam:
    """Represents a dynamically formed team of agents"""
    
    def __init__(self, task: ResearchTask):
        self.task = task
        self.agents = []
        self.formation_strategy = ""
        self.collaboration_pattern = ""
        
    def form_team(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Form the optimal agent team based on task analysis"""
        
        complexity = analysis["complexity"]
        skills = analysis["skills"]
        agent_count = analysis["agent_count"]
        
        # Define agent types and their capabilities
        agent_capabilities = {
            "IO": ["research", "general_reasoning", "synthesis"],
            "TOT": ["analysis", "deep_reasoning", "planning"],
            "WEB": ["web_search", "information_gathering", "fact_checking"],
            "CODE": ["coding", "technical_analysis", "algorithm_design"],
            "CREATIVE": ["creativity", "brainstorming", "design"],
            "CRITIC": ["evaluation", "quality_check", "verification"]
        }
        
        # Select agents based on required skills
        selected_agents = []
        
        # Always include at least one IO agent for coordination
        selected_agents.append("IO")
        
        # Add specialized agents based on skills
        for skill in skills:
            for agent_type, capabilities in agent_capabilities.items():
                if skill in capabilities and agent_type not in selected_agents:
                    selected_agents.append(agent_type)
                    break
        
        # Add TOT agent for complex tasks
        if complexity == "high" and "TOT" not in selected_agents:
            selected_agents.append("TOT")
        
        # Add additional IO agents if needed
        while len(selected_agents) < agent_count:
            selected_agents.append("IO")
        
        # Trim if too many agents
        selected_agents = selected_agents[:agent_count]
        
        self.agents = selected_agents
        self.formation_strategy = self._determine_formation_strategy(complexity, skills)
        self.collaboration_pattern = self._determine_collaboration_pattern(selected_agents)
        
        return {
            "agents": selected_agents,
            "formation_strategy": self.formation_strategy,
            "collaboration_pattern": self.collaboration_pattern,
            "estimated_performance": self._estimate_performance(selected_agents, skills)
        }
    
    def _determine_formation_strategy(self, complexity: str, skills: List[str]) -> str:
        """Determine the team formation strategy"""
        
        if complexity == "high" and len(skills) > 3:
            return "hierarchical_specialization"
        elif len(skills) > 2:
            return "skill_based_clustering"
        elif complexity == "high":
            return "deep_collaboration"
        else:
            return "simple_parallel"
    
    def _determine_collaboration_pattern(self, agents: List[str]) -> str:
        """Determine how agents will collaborate"""
        
        if len(agents) <= 2:
            return "sequential"
        elif "TOT" in agents:
            return "hub_and_spoke"
        elif len(agents) >= 4:
            return "fully_connected"
        else:
            return "pipeline"
    
    def _estimate_performance(self, agents: List[str], skills: List[str]) -> float:
        """Estimate team performance based on agent-skill matching"""
        
        agent_skill_map = {
            "IO": ["research", "synthesis"],
            "TOT": ["analysis", "deep_reasoning"],
            "WEB": ["web_search", "information_gathering"],
            "CODE": ["coding", "technical_analysis"],
            "CREATIVE": ["creativity", "design"],
            "CRITIC": ["evaluation", "verification"]
        }
        
        skill_coverage = 0
        for skill in skills:
            for agent in agents:
                if skill in agent_skill_map.get(agent, []):
                    skill_coverage += 1
                    break
        
        base_performance = 0.6
        skill_bonus = (skill_coverage / max(len(skills), 1)) * 0.3
        team_size_bonus = min(len(agents) / 4, 1) * 0.1
        
        return min(base_performance + skill_bonus + team_size_bonus, 1.0)

class AdvancedResearchAssistant:
    """Advanced research assistant with dynamic team formation"""
    
    def __init__(self):
        self.completed_tasks = []
        self.active_teams = {}
        self.performance_history = []
        
    async def process_research_query(self, query: str, domain: str = "general") -> Dict[str, Any]:
        """Process a research query with dynamic team formation"""
        
        print(f"\n🔬 Processing Research Query:")
        print(f"   Query: {query}")
        print(f"   Domain: {domain}")
        
        # Create research task
        task = ResearchTask(query, domain)
        
        # Analyze task complexity
        analysis = task.analyze_complexity()
        print(f"\n📊 Task Analysis:")
        print(f"   Complexity: {analysis['complexity']}")
        print(f"   Required Skills: {', '.join(analysis['skills'])}")
        print(f"   Estimated Time: {analysis['estimated_time']}s")
        print(f"   Recommended Agents: {analysis['agent_count']}")
        
        # Form optimal team
        team = AgentTeam(task)
        team_config = team.form_team(analysis)
        
        print(f"\n🤝 Team Formation:")
        print(f"   Agents: {', '.join(team_config['agents'])}")
        print(f"   Strategy: {team_config['formation_strategy']}")
        print(f"   Collaboration: {team_config['collaboration_pattern']}")
        print(f"   Expected Performance: {team_config['estimated_performance']:.1%}")
        
        # Simulate research execution
        execution_result = await self._execute_research(task, team, team_config)
        
        print(f"\n✅ Research Completed:")
        print(f"   Actual Performance: {execution_result['performance']:.1%}")
        print(f"   Time Taken: {execution_result['time_taken']:.1f}s")
        print(f"   Sources Found: {execution_result['sources_count']}")
        print(f"   Quality Score: {execution_result['quality_score']:.1f}/10")
        
        # Store results
        result = {
            "task": task,
            "analysis": analysis,
            "team_config": team_config,
            "execution_result": execution_result,
            "success": execution_result['performance'] > 0.7
        }
        
        self.completed_tasks.append(result)
        self.performance_history.append(execution_result['performance'])
        
        return result
    
    async def _execute_research(self, 
                              task: ResearchTask, 
                              team: AgentTeam, 
                              team_config: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate research execution with the formed team"""
        
        # Simulate research phases
        phases = [
            "Information Gathering",
            "Analysis & Processing", 
            "Synthesis & Integration",
            "Quality Review"
        ]
        
        total_time = 0
        sources_count = 0
        quality_scores = []
        
        for i, phase in enumerate(phases):
            print(f"   Phase {i+1}: {phase}...")
            
            # Simulate phase execution time
            phase_time = random.uniform(0.5, 2.0)
            total_time += phase_time
            await asyncio.sleep(0.1)  # Simulate processing
            
            # Simulate phase outcomes
            if phase == "Information Gathering":
                sources_count = random.randint(3, 15)
            elif phase == "Analysis & Processing":
                quality_scores.append(random.uniform(7.0, 9.5))
            elif phase == "Synthesis & Integration":
                quality_scores.append(random.uniform(6.5, 9.0))
            elif phase == "Quality Review":
                quality_scores.append(random.uniform(7.5, 9.5))
        
        # Calculate final performance
        base_performance = team_config['estimated_performance']
        execution_variance = random.uniform(-0.1, 0.1)
        actual_performance = max(0.0, min(1.0, base_performance + execution_variance))
        
        return {
            "performance": actual_performance,
            "time_taken": total_time,
            "sources_count": sources_count,
            "quality_score": sum(quality_scores) / len(quality_scores) if quality_scores else 7.0,
            "phases_completed": len(phases)
        }
    
    def get_performance_analytics(self) -> Dict[str, Any]:
        """Get performance analytics across all completed tasks"""
        
        if not self.completed_tasks:
            return {"message": "No tasks completed yet"}
        
        # Calculate metrics
        total_tasks = len(self.completed_tasks)
        successful_tasks = sum(1 for task in self.completed_tasks if task['success'])
        success_rate = successful_tasks / total_tasks
        
        avg_performance = sum(self.performance_history) / len(self.performance_history)
        
        # Analyze by complexity
        complexity_stats = {"low": [], "medium": [], "high": []}
        for task in self.completed_tasks:
            complexity = task['analysis']['complexity']
            performance = task['execution_result']['performance']
            complexity_stats[complexity].append(performance)
        
        complexity_averages = {}
        for complexity, performances in complexity_stats.items():
            if performances:
                complexity_averages[complexity] = sum(performances) / len(performances)
            else:
                complexity_averages[complexity] = 0.0
        
        # Analyze team configurations
        team_patterns = {}
        for task in self.completed_tasks:
            pattern = task['team_config']['collaboration_pattern']
            if pattern not in team_patterns:
                team_patterns[pattern] = []
            team_patterns[pattern].append(task['execution_result']['performance'])
        
        pattern_averages = {}
        for pattern, performances in team_patterns.items():
            pattern_averages[pattern] = sum(performances) / len(performances)
        
        return {
            "total_tasks": total_tasks,
            "success_rate": success_rate,
            "average_performance": avg_performance,
            "complexity_performance": complexity_averages,
            "team_pattern_performance": pattern_averages,
            "best_performing_pattern": max(pattern_averages.items(), key=lambda x: x[1])[0] if pattern_averages else None
        }

async def run_research_demo():
    """Run comprehensive research assistant demo"""
    
    print("🧠 Advanced Research Assistant Demo")
    print("=" * 50)
    
    assistant = AdvancedResearchAssistant()
    
    # Demo research queries of varying complexity
    demo_queries = [
        {
            "query": "What is machine learning?",
            "domain": "computer_science"
        },
        {
            "query": "Compare the effectiveness of renewable energy sources in reducing carbon emissions",
            "domain": "environmental_science"
        },
        {
            "query": "Analyze the impact of AI on healthcare delivery, including case studies and future implications",
            "domain": "healthcare"
        },
        {
            "query": "Design an algorithm for optimizing urban traffic flow using real-time data",
            "domain": "computer_science"
        },
        {
            "query": "Synthesize research on quantum computing applications in cryptography and propose novel approaches",
            "domain": "quantum_computing"
        }
    ]
    
    # Process each query
    results = []
    for i, query_data in enumerate(demo_queries, 1):
        print(f"\n{'='*20} TASK {i} {'='*20}")
        result = await assistant.process_research_query(
            query_data["query"], 
            query_data["domain"]
        )
        results.append(result)
        
        # Small delay between tasks
        await asyncio.sleep(0.5)
    
    # Display analytics
    print(f"\n{'='*20} ANALYTICS {'='*20}")
    analytics = assistant.get_performance_analytics()
    
    print(f"\n📈 Overall Performance:")
    print(f"   Total Tasks: {analytics['total_tasks']}")
    print(f"   Success Rate: {analytics['success_rate']:.1%}")
    print(f"   Average Performance: {analytics['average_performance']:.1%}")
    
    print(f"\n🎯 Performance by Complexity:")
    for complexity, avg_perf in analytics['complexity_performance'].items():
        print(f"   {complexity.title()}: {avg_perf:.1%}")
    
    print(f"\n🤝 Performance by Team Pattern:")
    for pattern, avg_perf in analytics['team_pattern_performance'].items():
        print(f"   {pattern.title().replace('_', ' ')}: {avg_perf:.1%}")
    
    if analytics['best_performing_pattern']:
        print(f"\n🏆 Best Team Pattern: {analytics['best_performing_pattern'].title().replace('_', ' ')}")
    
    print(f"\n🔍 Insights:")
    
    # Generate insights
    insights = []
    
    if analytics['complexity_performance']['high'] > analytics['complexity_performance']['low']:
        insights.append("Complex tasks benefit from specialized agent teams")
    
    if analytics['average_performance'] > 0.8:
        insights.append("Dynamic team formation is highly effective")
    elif analytics['average_performance'] > 0.6:
        insights.append("Good performance with room for optimization")
    else:
        insights.append("Team formation strategy needs refinement")
    
    best_pattern = analytics.get('best_performing_pattern', '')
    if 'fully_connected' in best_pattern:
        insights.append("Full connectivity enhances collaboration")
    elif 'hub_and_spoke' in best_pattern:
        insights.append("Centralized coordination works well")
    
    for insight in insights:
        print(f"   • {insight}")
    
    return results, analytics

if __name__ == "__main__":
    asyncio.run(run_research_demo())