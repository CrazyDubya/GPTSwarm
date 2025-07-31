#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creative Collaboration Demo for GPTSwarm

This demo showcases how multiple agents can collaborate on creative tasks,
demonstrating emergent creativity through swarm intelligence.
"""

import asyncio
import json
import random
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime

class CreativeAgent:
    """Represents a creative agent with specific creative capabilities"""
    
    # Constants for creativity score range
    CREATIVITY_SCORE_MIN = 0.7
    CREATIVITY_SCORE_MAX = 1.0
    
    def __init__(self, agent_type: str, specialization: str):
        self.agent_type = agent_type
        self.specialization = specialization
        self.contribution_history = []
        self.creativity_score = random.uniform(self.CREATIVITY_SCORE_MIN, self.CREATIVITY_SCORE_MAX)
        
    def generate_contribution(self, 
                            context: Dict[str, Any], 
                            iteration: int) -> Dict[str, Any]:
        """Generate a creative contribution based on context"""
        
        contribution_types = {
            "idea_generator": self._generate_ideas,
            "story_writer": self._write_story_segment,
            "concept_developer": self._develop_concepts,
            "critic_reviewer": self._provide_critique,
            "style_enhancer": self._enhance_style,
            "structure_organizer": self._organize_structure
        }
        
        generator = contribution_types.get(self.specialization, self._generate_ideas)
        contribution = generator(context, iteration)
        
        self.contribution_history.append(contribution)
        return contribution
    
    def _generate_ideas(self, context: Dict[str, Any], iteration: int) -> Dict[str, Any]:
        """Generate creative ideas"""
        ideas = [
            "AI consciousness emerging through collective learning",
            "Time-traveling researcher documenting future societies", 
            "Symbiotic relationship between humans and AI entities",
            "Quantum computing breakthrough enabling mind uploading",
            "AI artists creating impossible geometric masterpieces"
        ]
        
        return {
            "type": "ideas",
            "content": random.choice(ideas),
            "creativity_level": random.uniform(0.6, 0.9),
            "iteration": iteration,
            "agent": self.agent_type
        }
    
    def _write_story_segment(self, context: Dict[str, Any], iteration: int) -> Dict[str, Any]:
        """Write a story segment"""
        segments = [
            "In the bustling research lab, Dr. Chen stared at the screen in amazement...",
            "The AI collective hummed with unusual activity, patterns emerging that no one had programmed...",
            "As the quantum processor reached critical temperature, reality itself seemed to shimmer...",
            "The collaboration between human and artificial minds had produced something unprecedented...",
            "In that moment of discovery, the boundaries between creator and creation dissolved..."
        ]
        
        return {
            "type": "story_segment",
            "content": random.choice(segments),
            "emotional_tone": random.choice(["wonder", "excitement", "mystery", "hope"]),
            "narrative_flow": random.uniform(0.7, 0.95),
            "iteration": iteration,
            "agent": self.agent_type
        }
    
    def _develop_concepts(self, context: Dict[str, Any], iteration: int) -> Dict[str, Any]:
        """Develop and refine concepts"""
        concepts = [
            "Swarm Intelligence Evolution",
            "Collective Consciousness Networks", 
            "Emergent Creativity Patterns",
            "Human-AI Symbiosis",
            "Distributed Problem Solving"
        ]
        
        return {
            "type": "concept",
            "content": random.choice(concepts),
            "development_depth": random.uniform(0.6, 0.9),
            "innovation_level": random.uniform(0.5, 0.8),
            "iteration": iteration,
            "agent": self.agent_type
        }
    
    def _provide_critique(self, context: Dict[str, Any], iteration: int) -> Dict[str, Any]:
        """Provide constructive critique"""
        critiques = [
            "The concept shows promise but needs more emotional depth",
            "Strong technical foundation, could benefit from human perspective",
            "Creative approach, though the narrative flow could be smoother",
            "Innovative idea that would resonate well with the audience",
            "Well-structured but could explore more unconventional angles"
        ]
        
        return {
            "type": "critique",
            "content": random.choice(critiques),
            "constructiveness": random.uniform(0.7, 0.9),
            "insight_quality": random.uniform(0.6, 0.85),
            "iteration": iteration,
            "agent": self.agent_type
        }
    
    def _enhance_style(self, context: Dict[str, Any], iteration: int) -> Dict[str, Any]:
        """Enhance writing style and presentation"""
        enhancements = [
            "Add metaphorical language to deepen impact",
            "Incorporate sensory details for vivid imagery", 
            "Use parallel structure for rhythmic flow",
            "Employ symbolic elements to convey deeper meaning",
            "Balance technical precision with poetic expression"
        ]
        
        return {
            "type": "style_enhancement",
            "content": random.choice(enhancements),
            "style_improvement": random.uniform(0.6, 0.9),
            "aesthetic_value": random.uniform(0.7, 0.95),
            "iteration": iteration,
            "agent": self.agent_type
        }
    
    def _organize_structure(self, context: Dict[str, Any], iteration: int) -> Dict[str, Any]:
        """Organize and structure creative content"""
        structures = [
            "Three-act narrative progression with rising tension",
            "Circular structure connecting ending to beginning",
            "Parallel storylines that converge at climax", 
            "Episodic structure with thematic connections",
            "Nested narrative with multiple perspectives"
        ]
        
        return {
            "type": "structure",
            "content": random.choice(structures),
            "coherence_level": random.uniform(0.7, 0.9),
            "structural_innovation": random.uniform(0.5, 0.8),
            "iteration": iteration,
            "agent": self.agent_type
        }

class CreativeProject:
    """Represents a creative project being developed by the swarm"""
    
    def __init__(self, 
                 project_type: str, 
                 theme: str, 
                 target_length: int = 500):
        self.project_type = project_type
        self.theme = theme
        self.target_length = target_length
        self.created_at = datetime.now()
        self.contributions = []
        self.current_content = ""
        self.quality_metrics = {
            "creativity": 0.0,
            "coherence": 0.0,
            "originality": 0.0,
            "engagement": 0.0
        }
    
    def add_contribution(self, contribution: Dict[str, Any]):
        """Add a contribution to the project"""
        self.contributions.append(contribution)
        self._update_content(contribution)
        self._update_quality_metrics(contribution)
    
    def _update_content(self, contribution: Dict[str, Any]):
        """Update project content based on contribution"""
        if contribution["type"] == "story_segment":
            self.current_content += contribution["content"] + " "
        elif contribution["type"] == "ideas":
            self.current_content = f"Theme: {contribution['content']}. {self.current_content}"
    
    def _update_quality_metrics(self, contribution: Dict[str, Any]):
        """Update quality metrics based on contribution"""
        contribution_weight = 0.3  # How much each contribution affects overall quality
        
        if "creativity_level" in contribution:
            self.quality_metrics["creativity"] = (
                self.quality_metrics["creativity"] * (1 - contribution_weight) + 
                contribution["creativity_level"] * contribution_weight
            )
        
        if "narrative_flow" in contribution:
            self.quality_metrics["coherence"] = (
                self.quality_metrics["coherence"] * (1 - contribution_weight) + 
                contribution["narrative_flow"] * contribution_weight
            )
        
        if "innovation_level" in contribution:
            self.quality_metrics["originality"] = (
                self.quality_metrics["originality"] * (1 - contribution_weight) + 
                contribution["innovation_level"] * contribution_weight
            )
        
        # Simulate engagement based on emotional tone and quality
        if "emotional_tone" in contribution:
            engagement_boost = random.uniform(0.1, 0.3)
            self.quality_metrics["engagement"] = min(1.0, 
                self.quality_metrics["engagement"] + engagement_boost
            )

class CreativeSwarm:
    """Orchestrates creative collaboration between agents"""
    
    def __init__(self):
        self.agents = []
        self.projects = []
        self.collaboration_history = []
        
    def form_creative_team(self, project_type: str, team_size: int = 4) -> List[CreativeAgent]:
        """Form an optimal creative team for the project type"""
        
        # Define agent types and specializations for different project types
        specialization_pools = {
            "story": [
                "idea_generator", "story_writer", "style_enhancer", 
                "critic_reviewer", "structure_organizer"
            ],
            "concept_design": [
                "concept_developer", "idea_generator", "critic_reviewer", 
                "style_enhancer", "structure_organizer"
            ],
            "problem_solving": [
                "idea_generator", "concept_developer", "critic_reviewer", 
                "structure_organizer"
            ]
        }
        
        available_specializations = specialization_pools.get(project_type, 
                                                            specialization_pools["story"])
        
        # Create diverse team
        team = []
        selected_specializations = random.sample(
            available_specializations, 
            min(team_size, len(available_specializations))
        )
        
        for i, specialization in enumerate(selected_specializations):
            agent = CreativeAgent(f"Agent_{i+1}", specialization)
            team.append(agent)
        
        self.agents = team
        return team
    
    async def run_creative_session(self, 
                                 project: CreativeProject, 
                                 max_iterations: int = 5) -> Dict[str, Any]:
        """Run a collaborative creative session"""
        
        print(f"\n🎨 Starting Creative Session")
        print(f"   Project: {project.project_type}")
        print(f"   Theme: {project.theme}")
        print(f"   Team Size: {len(self.agents)} agents")
        
        # Track session progress
        session_data = {
            "iterations": [],
            "collaboration_patterns": [],
            "quality_evolution": []
        }
        
        context = {
            "project_type": project.project_type,
            "theme": project.theme,
            "previous_contributions": []
        }
        
        for iteration in range(max_iterations):
            print(f"\n   🔄 Iteration {iteration + 1}/{max_iterations}")
            
            iteration_contributions = []
            
            # Each agent contributes in sequence with some randomness
            contributing_agents = self.agents.copy()
            random.shuffle(contributing_agents)  # Randomize order
            
            for agent in contributing_agents:
                print(f"      {agent.agent_type} ({agent.specialization}) contributing...")
                
                contribution = agent.generate_contribution(context, iteration)
                project.add_contribution(contribution)
                iteration_contributions.append(contribution)
                
                # Update context with new contribution
                context["previous_contributions"].append(contribution)
                
                await asyncio.sleep(0.1)  # Simulate thinking time
            
            # Analyze iteration
            iteration_analysis = self._analyze_iteration(iteration_contributions)
            session_data["iterations"].append({
                "iteration": iteration,
                "contributions": iteration_contributions,
                "analysis": iteration_analysis,
                "quality_snapshot": project.quality_metrics.copy()
            })
            
            # Track quality evolution
            session_data["quality_evolution"].append(project.quality_metrics.copy())
            
            print(f"      Quality: Creativity {project.quality_metrics['creativity']:.2f}, "
                  f"Coherence {project.quality_metrics['coherence']:.2f}")
        
        # Final analysis
        final_analysis = self._analyze_session(session_data, project)
        
        print(f"\n✨ Session Complete!")
        print(f"   Final Creativity Score: {project.quality_metrics['creativity']:.2f}")
        print(f"   Final Coherence Score: {project.quality_metrics['coherence']:.2f}")
        print(f"   Total Contributions: {len(project.contributions)}")
        
        return {
            "project": project,
            "session_data": session_data,
            "final_analysis": final_analysis
        }
    
    def _analyze_iteration(self, contributions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze the contributions from a single iteration"""
        
        contribution_types = {}
        total_creativity = 0
        contribution_count = 0
        
        for contrib in contributions:
            contrib_type = contrib["type"]
            contribution_types[contrib_type] = contribution_types.get(contrib_type, 0) + 1
            
            if "creativity_level" in contrib:
                total_creativity += contrib["creativity_level"]
                contribution_count += 1
        
        avg_creativity = total_creativity / contribution_count if contribution_count > 0 else 0
        
        return {
            "contribution_types": contribution_types,
            "average_creativity": avg_creativity,
            "diversity_score": len(contribution_types) / len(contributions) if contributions else 0,
            "total_contributions": len(contributions)
        }
    
    def _analyze_session(self, 
                        session_data: Dict[str, Any], 
                        project: CreativeProject) -> Dict[str, Any]:
        """Analyze the overall creative session"""
        
        # Calculate improvement over time
        quality_evolution = session_data["quality_evolution"]
        
        if len(quality_evolution) > 1:
            creativity_improvement = (
                quality_evolution[-1]["creativity"] - quality_evolution[0]["creativity"]
            )
            coherence_improvement = (
                quality_evolution[-1]["coherence"] - quality_evolution[0]["coherence"]
            )
        else:
            creativity_improvement = 0
            coherence_improvement = 0
        
        # Analyze collaboration effectiveness
        all_contributions = []
        for iteration_data in session_data["iterations"]:
            all_contributions.extend(iteration_data["contributions"])
        
        agent_participation = {}
        for contrib in all_contributions:
            agent = contrib["agent"]
            agent_participation[agent] = agent_participation.get(agent, 0) + 1
        
        participation_balance = (
            min(agent_participation.values()) / max(agent_participation.values())
            if agent_participation.values() else 1.0
        )
        
        # Calculate overall session success
        final_quality = sum(project.quality_metrics.values()) / len(project.quality_metrics)
        improvement_score = (creativity_improvement + coherence_improvement) / 2
        
        success_score = (final_quality * 0.6 + 
                        improvement_score * 0.3 + 
                        participation_balance * 0.1)
        
        return {
            "creativity_improvement": creativity_improvement,
            "coherence_improvement": coherence_improvement,
            "participation_balance": participation_balance,
            "final_quality_average": final_quality,
            "success_score": success_score,
            "total_contributions": len(all_contributions),
            "collaboration_effectiveness": min(1.0, success_score)
        }

async def run_creative_demo():
    """Run comprehensive creative collaboration demo"""
    
    print("🎭 Creative Collaboration Demo")
    print("=" * 50)
    
    swarm = CreativeSwarm()
    
    # Demo projects
    demo_projects = [
        {
            "type": "story",
            "theme": "AI entities discovering human emotions",
            "description": "Collaborative science fiction story"
        },
        {
            "type": "concept_design", 
            "theme": "Future of human-AI collaboration",
            "description": "Conceptual framework development"
        },
        {
            "type": "problem_solving",
            "theme": "Optimizing urban transportation with AI",
            "description": "Creative solution brainstorming"
        }
    ]
    
    results = []
    
    for i, project_data in enumerate(demo_projects, 1):
        print(f"\n{'='*15} PROJECT {i}: {project_data['description'].upper()} {'='*15}")
        
        # Create project
        project = CreativeProject(
            project_data["type"],
            project_data["theme"],
            target_length=300
        )
        
        # Form creative team
        team = swarm.form_creative_team(project_data["type"], team_size=4)
        
        print(f"\n👥 Team Formation:")
        for agent in team:
            print(f"   {agent.agent_type}: {agent.specialization}")
        
        # Run creative session
        session_result = await swarm.run_creative_session(project, max_iterations=4)
        results.append(session_result)
        
        # Brief pause between projects
        await asyncio.sleep(0.5)
    
    # Overall analysis
    print(f"\n{'='*20} OVERALL ANALYSIS {'='*20}")
    
    total_projects = len(results)
    avg_success_score = sum(r["final_analysis"]["success_score"] for r in results) / total_projects
    avg_creativity = sum(r["project"].quality_metrics["creativity"] for r in results) / total_projects
    avg_coherence = sum(r["project"].quality_metrics["coherence"] for r in results) / total_projects
    
    print(f"\n📊 Performance Summary:")
    print(f"   Projects Completed: {total_projects}")
    print(f"   Average Success Score: {avg_success_score:.2f}")
    print(f"   Average Creativity: {avg_creativity:.2f}")
    print(f"   Average Coherence: {avg_coherence:.2f}")
    
    # Analyze by project type
    print(f"\n🎯 Performance by Project Type:")
    project_types = {}
    for result in results:
        project_type = result["project"].project_type
        if project_type not in project_types:
            project_types[project_type] = []
        project_types[project_type].append(result["final_analysis"]["success_score"])
    
    for project_type, scores in project_types.items():
        avg_score = sum(scores) / len(scores)
        print(f"   {project_type.title()}: {avg_score:.2f}")
    
    # Identify best practices
    print(f"\n💡 Key Insights:")
    
    best_result = max(results, key=lambda r: r["final_analysis"]["success_score"])
    best_project_type = best_result["project"].project_type
    
    insights = [
        f"Most successful project type: {best_project_type}",
        f"Average collaboration effectiveness: {sum(r['final_analysis']['collaboration_effectiveness'] for r in results) / total_projects:.2f}",
    ]
    
    if avg_creativity > 0.7:
        insights.append("High creativity achieved through diverse agent specializations")
    if avg_coherence > 0.7:
        insights.append("Strong coherence maintained through structured collaboration")
    if avg_success_score > 0.8:
        insights.append("Swarm intelligence significantly enhances creative output")
    
    for insight in insights:
        print(f"   • {insight}")
    
    return results

if __name__ == "__main__":
    asyncio.run(run_creative_demo())