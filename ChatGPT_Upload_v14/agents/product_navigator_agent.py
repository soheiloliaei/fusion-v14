#!/usr/bin/env python3
"""
Product Navigator Agent - Fusion v14
Maps feature requirements, dev viability, edge cases, complexity scoring
"""

import asyncio
import time
import logging
import re
from typing import Dict, Any, List, Optional
from datetime import datetime

class ProductNavigatorAgent:
    """
    Product Navigator Agent - Fusion v14
    Maps feature requirements, dev viability, edge cases, complexity scoring
    """
    
    def __init__(self):
        self.logger = logging.getLogger("ProductNavigatorAgent")
        
        # Feature complexity levels
        self.complexity_levels = {
            "simple": {"score": 1, "description": "Basic feature with minimal complexity", "dev_time": "1-2 weeks"},
            "moderate": {"score": 2, "description": "Standard feature with some complexity", "dev_time": "2-4 weeks"},
            "complex": {"score": 3, "description": "Advanced feature with significant complexity", "dev_time": "4-8 weeks"},
            "expert": {"score": 4, "description": "Highly complex feature requiring specialized knowledge", "dev_time": "8+ weeks"}
        }
        
        # Risk categories
        self.risk_categories = {
            "technical": ["performance", "scalability", "security", "compatibility"],
            "business": ["user_adoption", "revenue_impact", "competitive_position", "regulatory"],
            "operational": ["maintenance", "support", "training", "documentation"]
        }
        
        # Edge case patterns
        self.edge_case_patterns = {
            "data": ["empty_state", "large_datasets", "invalid_input", "network_failure"],
            "user": ["new_user", "power_user", "accessibility_needs", "international"],
            "system": ["offline_mode", "slow_connection", "browser_compatibility", "mobile_responsive"],
            "business": ["compliance", "audit_trail", "data_privacy", "rate_limiting"]
        }
        
        # Viability criteria
        self.viability_criteria = {
            "technical_feasibility": ["existing_infrastructure", "team_expertise", "third_party_dependencies"],
            "business_value": ["user_impact", "revenue_potential", "strategic_alignment"],
            "resource_availability": ["budget", "timeline", "team_capacity", "priority_level"]
        }
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Product Navigator Agent
        """
        start_time = time.time()
        self.logger.info("Product Navigator Agent starting analysis")
        
        try:
            # Analyze feature requirements
            feature_analysis = await self._analyze_feature_requirements(prompt)
            
            # Assess development viability
            viability_assessment = await self._assess_development_viability(prompt, feature_analysis)
            
            # Identify edge cases
            edge_case_analysis = await self._identify_edge_cases(prompt, feature_analysis)
            
            # Calculate complexity score
            complexity_assessment = await self._calculate_complexity_score(prompt, feature_analysis, edge_case_analysis)
            
            # Generate risk assessment
            risk_assessment = await self._generate_risk_assessment(prompt, feature_analysis, edge_case_analysis)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, feature_analysis, viability_assessment, edge_case_analysis, complexity_assessment, risk_assessment)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(feature_analysis, viability_assessment, complexity_assessment)
            
            self.logger.info(f"Product Navigator Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "feature_analysis": feature_analysis,
                "viability_assessment": viability_assessment,
                "edge_case_analysis": edge_case_analysis,
                "complexity_assessment": complexity_assessment,
                "risk_assessment": risk_assessment,
                "execution_time": execution_time,
                "shared_state": {
                    "feature_type": feature_analysis.get("feature_type"),
                    "complexity_level": complexity_assessment.get("level"),
                    "viability_score": viability_assessment.get("overall_score"),
                    "risk_level": risk_assessment.get("overall_risk_level"),
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Product Navigator Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
    
    async def _analyze_feature_requirements(self, prompt: str) -> Dict[str, Any]:
        """Analyze feature requirements from prompt"""
        
        prompt_lower = prompt.lower()
        
        # Detect feature type
        feature_type = self._detect_feature_type(prompt_lower)
        
        # Identify functional requirements
        functional_requirements = self._identify_functional_requirements(prompt_lower)
        
        # Extract non-functional requirements
        non_functional_requirements = self._extract_non_functional_requirements(prompt_lower)
        
        # Determine user impact
        user_impact = self._determine_user_impact(prompt_lower)
        
        return {
            "feature_type": feature_type,
            "functional_requirements": functional_requirements,
            "non_functional_requirements": non_functional_requirements,
            "user_impact": user_impact,
            "priority_level": self._determine_priority_level(prompt_lower)
        }
    
    async def _assess_development_viability(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Assess development viability"""
        
        # Technical feasibility
        technical_feasibility = self._assess_technical_feasibility(prompt, feature_analysis)
        
        # Business value assessment
        business_value = self._assess_business_value(prompt, feature_analysis)
        
        # Resource availability
        resource_availability = self._assess_resource_availability(prompt, feature_analysis)
        
        # Calculate overall viability score
        overall_score = self._calculate_viability_score(technical_feasibility, business_value, resource_availability)
        
        return {
            "technical_feasibility": technical_feasibility,
            "business_value": business_value,
            "resource_availability": resource_availability,
            "overall_score": overall_score,
            "recommendation": self._generate_viability_recommendation(overall_score)
        }
    
    async def _identify_edge_cases(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Identify potential edge cases"""
        
        edge_cases = []
        edge_case_categories = {}
        
        # Identify data-related edge cases
        data_edge_cases = self._identify_data_edge_cases(prompt, feature_analysis)
        if data_edge_cases:
            edge_case_categories["data"] = data_edge_cases
            edge_cases.extend(data_edge_cases)
        
        # Identify user-related edge cases
        user_edge_cases = self._identify_user_edge_cases(prompt, feature_analysis)
        if user_edge_cases:
            edge_case_categories["user"] = user_edge_cases
            edge_cases.extend(user_edge_cases)
        
        # Identify system-related edge cases
        system_edge_cases = self._identify_system_edge_cases(prompt, feature_analysis)
        if system_edge_cases:
            edge_case_categories["system"] = system_edge_cases
            edge_cases.extend(system_edge_cases)
        
        # Identify business-related edge cases
        business_edge_cases = self._identify_business_edge_cases(prompt, feature_analysis)
        if business_edge_cases:
            edge_case_categories["business"] = business_edge_cases
            edge_cases.extend(business_edge_cases)
        
        return {
            "edge_cases": edge_cases,
            "edge_case_categories": edge_case_categories,
            "total_edge_cases": len(edge_cases),
            "critical_edge_cases": self._identify_critical_edge_cases(edge_cases)
        }
    
    async def _calculate_complexity_score(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> Dict[str, Any]:
        """Calculate complexity score"""
        
        # Analyze complexity factors
        complexity_factors = self._analyze_complexity_factors(prompt, feature_analysis, edge_case_analysis)
        
        # Calculate base complexity score
        base_score = self._calculate_base_complexity_score(complexity_factors)
        
        # Adjust for edge cases
        edge_case_adjustment = self._calculate_edge_case_adjustment(edge_case_analysis)
        
        # Final complexity score
        final_score = min(base_score + edge_case_adjustment, 4.0)
        complexity_level = self._determine_complexity_level(final_score)
        
        return {
            "level": complexity_level,
            "score": final_score,
            "factors": complexity_factors,
            "edge_case_adjustment": edge_case_adjustment,
            "description": self.complexity_levels[complexity_level]["description"],
            "estimated_dev_time": self.complexity_levels[complexity_level]["dev_time"]
        }
    
    async def _generate_risk_assessment(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> Dict[str, Any]:
        """Generate comprehensive risk assessment"""
        
        # Technical risks
        technical_risks = self._assess_technical_risks(prompt, feature_analysis, edge_case_analysis)
        
        # Business risks
        business_risks = self._assess_business_risks(prompt, feature_analysis, edge_case_analysis)
        
        # Operational risks
        operational_risks = self._assess_operational_risks(prompt, feature_analysis, edge_case_analysis)
        
        # Calculate overall risk level
        overall_risk_level = self._calculate_overall_risk_level(technical_risks, business_risks, operational_risks)
        
        return {
            "technical_risks": technical_risks,
            "business_risks": business_risks,
            "operational_risks": operational_risks,
            "overall_risk_level": overall_risk_level,
            "risk_mitigation_strategies": self._generate_risk_mitigation_strategies(overall_risk_level)
        }
    
    async def _create_enhanced_output(self, prompt: str, feature_analysis: Dict, viability_assessment: Dict, edge_case_analysis: Dict, complexity_assessment: Dict, risk_assessment: Dict) -> str:
        """Create enhanced output with comprehensive analysis"""
        
        return f"""# Product Navigator Analysis & Assessment

## Original Request
{prompt}

## Feature Analysis

### Feature Type
**Type:** {feature_analysis.get('feature_type', 'unknown').title()}
**Priority Level:** {feature_analysis.get('priority_level', 'medium').title()}
**User Impact:** {feature_analysis.get('user_impact', 'medium').title()}

### Functional Requirements
{self._format_requirements(feature_analysis.get('functional_requirements', []))}

### Non-Functional Requirements
{self._format_requirements(feature_analysis.get('non_functional_requirements', []))}

## Development Viability

### Technical Feasibility
**Score:** {viability_assessment.get('technical_feasibility', {}).get('score', 0):.2f}/1.00
**Factors:** {', '.join(viability_assessment.get('technical_feasibility', {}).get('factors', ['None identified']))}

### Business Value
**Score:** {viability_assessment.get('business_value', {}).get('score', 0):.2f}/1.00
**Factors:** {', '.join(viability_assessment.get('business_value', {}).get('factors', ['None identified']))}

### Resource Availability
**Score:** {viability_assessment.get('resource_availability', {}).get('score', 0):.2f}/1.00
**Factors:** {', '.join(viability_assessment.get('resource_availability', {}).get('factors', ['None identified']))}

### Overall Viability
**Score:** {viability_assessment.get('overall_score', 0):.2f}/1.00
**Recommendation:** {viability_assessment.get('recommendation', 'No recommendation available')}

## Edge Case Analysis

### Identified Edge Cases ({edge_case_analysis.get('total_edge_cases', 0)} total)
{self._format_edge_cases(edge_case_analysis.get('edge_case_categories', {}))}

### Critical Edge Cases
{self._format_critical_edge_cases(edge_case_analysis.get('critical_edge_cases', []))}

## Complexity Assessment

### Level: {complexity_assessment.get('level', 'unknown').upper()}
**Score:** {complexity_assessment.get('score', 0):.1f}/4.0
**Description:** {complexity_assessment.get('description', 'No description available')}
**Estimated Development Time:** {complexity_assessment.get('estimated_dev_time', 'Unknown')}

### Complexity Factors
{self._format_complexity_factors(complexity_assessment.get('factors', {}))}

## Risk Assessment

### Overall Risk Level: {risk_assessment.get('overall_risk_level', 'unknown').upper()}

### Technical Risks
{self._format_risks(risk_assessment.get('technical_risks', []))}

### Business Risks
{self._format_risks(risk_assessment.get('business_risks', []))}

### Operational Risks
{self._format_risks(risk_assessment.get('operational_risks', []))}

### Risk Mitigation Strategies
{self._format_mitigation_strategies(risk_assessment.get('risk_mitigation_strategies', []))}

## Product Navigator Confidence
**Score:** {self._calculate_confidence(feature_analysis, viability_assessment, complexity_assessment):.2f}/1.00

*Generated by Fusion v14 Product Navigator Agent*"""
    
    def _detect_feature_type(self, prompt: str) -> str:
        """Detect feature type from prompt"""
        if any(word in prompt for word in ["tracker", "tracking", "monitor"]):
            return "tracking_feature"
        elif any(word in prompt for word in ["dispute", "conflict", "resolution"]):
            return "dispute_management"
        elif any(word in prompt for word in ["payment", "billing", "invoice"]):
            return "payment_processing"
        elif any(word in prompt for word in ["notification", "alert", "reminder"]):
            return "notification_system"
        elif any(word in prompt for word in ["report", "analytics", "dashboard"]):
            return "reporting_analytics"
        elif any(word in prompt for word in ["user", "profile", "account"]):
            return "user_management"
        else:
            return "general_feature"
    
    def _identify_functional_requirements(self, prompt: str) -> List[str]:
        """Identify functional requirements"""
        requirements = []
        
        if any(word in prompt for word in ["track", "monitor", "log"]):
            requirements.append("data_tracking")
        
        if any(word in prompt for word in ["search", "filter", "sort"]):
            requirements.append("search_filtering")
        
        if any(word in prompt for word in ["export", "download", "report"]):
            requirements.append("data_export")
        
        if any(word in prompt for word in ["notify", "alert", "email"]):
            requirements.append("notifications")
        
        if any(word in prompt for word in ["approve", "reject", "workflow"]):
            requirements.append("approval_workflow")
        
        return requirements
    
    def _extract_non_functional_requirements(self, prompt: str) -> List[str]:
        """Extract non-functional requirements"""
        requirements = []
        
        if any(word in prompt for word in ["fast", "performance", "speed"]):
            requirements.append("performance")
        
        if any(word in prompt for word in ["secure", "privacy", "encryption"]):
            requirements.append("security")
        
        if any(word in prompt for word in ["mobile", "responsive", "tablet"]):
            requirements.append("responsive_design")
        
        if any(word in prompt for word in ["accessible", "a11y", "disability"]):
            requirements.append("accessibility")
        
        return requirements
    
    def _determine_user_impact(self, prompt: str) -> str:
        """Determine user impact level"""
        if any(word in prompt for word in ["critical", "essential", "must"]):
            return "high"
        elif any(word in prompt for word in ["important", "significant", "major"]):
            return "medium"
        else:
            return "low"
    
    def _determine_priority_level(self, prompt: str) -> str:
        """Determine priority level"""
        if any(word in prompt for word in ["urgent", "critical", "immediate"]):
            return "high"
        elif any(word in prompt for word in ["important", "soon", "next"]):
            return "medium"
        else:
            return "low"
    
    def _assess_technical_feasibility(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Assess technical feasibility"""
        factors = []
        score = 0.8  # Base score
        
        # Check for existing infrastructure
        if feature_analysis.get("feature_type") in ["tracking_feature", "user_management"]:
            factors.append("existing_infrastructure")
            score += 0.1
        
        # Check for team expertise
        if feature_analysis.get("feature_type") != "expert_feature":
            factors.append("team_expertise")
            score += 0.1
        
        # Check for third-party dependencies
        if not any(word in prompt for word in ["external", "api", "integration"]):
            factors.append("minimal_dependencies")
            score += 0.1
        
        return {
            "score": min(score, 1.0),
            "factors": factors
        }
    
    def _assess_business_value(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Assess business value"""
        factors = []
        score = 0.7  # Base score
        
        # User impact
        user_impact = feature_analysis.get("user_impact", "low")
        if user_impact == "high":
            factors.append("high_user_impact")
            score += 0.2
        elif user_impact == "medium":
            factors.append("medium_user_impact")
            score += 0.1
        
        # Strategic alignment
        if feature_analysis.get("feature_type") in ["dispute_management", "payment_processing"]:
            factors.append("strategic_alignment")
            score += 0.1
        
        return {
            "score": min(score, 1.0),
            "factors": factors
        }
    
    def _assess_resource_availability(self, prompt: str, feature_analysis: Dict) -> Dict[str, Any]:
        """Assess resource availability"""
        factors = []
        score = 0.8  # Base score
        
        # Priority level
        priority = feature_analysis.get("priority_level", "low")
        if priority == "high":
            factors.append("high_priority")
            score += 0.1
        elif priority == "medium":
            factors.append("medium_priority")
            score += 0.05
        
        # Feature complexity
        if feature_analysis.get("feature_type") in ["general_feature", "user_management"]:
            factors.append("manageable_complexity")
            score += 0.1
        
        return {
            "score": min(score, 1.0),
            "factors": factors
        }
    
    def _calculate_viability_score(self, technical_feasibility: Dict, business_value: Dict, resource_availability: Dict) -> float:
        """Calculate overall viability score"""
        technical_score = technical_feasibility.get("score", 0.0)
        business_score = business_value.get("score", 0.0)
        resource_score = resource_availability.get("score", 0.0)
        
        # Weighted average
        return (technical_score * 0.4 + business_score * 0.4 + resource_score * 0.2)
    
    def _generate_viability_recommendation(self, overall_score: float) -> str:
        """Generate viability recommendation"""
        if overall_score >= 0.8:
            return "Highly viable - proceed with development"
        elif overall_score >= 0.6:
            return "Viable - proceed with some considerations"
        elif overall_score >= 0.4:
            return "Moderately viable - requires additional planning"
        else:
            return "Low viability - reconsider approach"
    
    def _identify_data_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify data-related edge cases"""
        edge_cases = []
        
        if any(word in prompt for word in ["track", "log", "data"]):
            edge_cases.extend(["empty_data_state", "large_dataset_handling", "data_validation"])
        
        if any(word in prompt for word in ["search", "filter"]):
            edge_cases.extend(["no_search_results", "special_characters", "unicode_support"])
        
        return edge_cases
    
    def _identify_user_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify user-related edge cases"""
        edge_cases = []
        
        edge_cases.extend(["new_user_experience", "power_user_workflows", "accessibility_needs"])
        
        if any(word in prompt for word in ["international", "global", "locale"]):
            edge_cases.extend(["internationalization", "timezone_handling", "currency_formatting"])
        
        return edge_cases
    
    def _identify_system_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify system-related edge cases"""
        edge_cases = []
        
        edge_cases.extend(["network_failure", "slow_connection", "browser_compatibility"])
        
        if any(word in prompt for word in ["mobile", "responsive"]):
            edge_cases.extend(["mobile_performance", "touch_interactions", "screen_size_variations"])
        
        return edge_cases
    
    def _identify_business_edge_cases(self, prompt: str, feature_analysis: Dict) -> List[str]:
        """Identify business-related edge cases"""
        edge_cases = []
        
        if any(word in prompt for word in ["compliance", "audit", "regulatory"]):
            edge_cases.extend(["compliance_requirements", "audit_trail", "data_retention"])
        
        if any(word in prompt for word in ["payment", "billing", "financial"]):
            edge_cases.extend(["payment_failures", "refund_processing", "fraud_detection"])
        
        return edge_cases
    
    def _identify_critical_edge_cases(self, edge_cases: List[str]) -> List[str]:
        """Identify critical edge cases"""
        critical_patterns = ["security", "compliance", "payment", "fraud", "data_loss"]
        return [case for case in edge_cases if any(pattern in case for pattern in critical_patterns)]
    
    def _analyze_complexity_factors(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> Dict[str, Any]:
        """Analyze complexity factors"""
        factors = {
            "integration_points": 0,
            "data_processing": 0,
            "user_interactions": 0,
            "business_logic": 0,
            "edge_cases": 0
        }
        
        # Integration points
        if any(word in prompt for word in ["api", "external", "integration"]):
            factors["integration_points"] = 1
        
        # Data processing
        if any(word in prompt for word in ["track", "log", "analyze", "process"]):
            factors["data_processing"] = 1
        
        # User interactions
        if any(word in prompt for word in ["interactive", "real-time", "dynamic"]):
            factors["user_interactions"] = 1
        
        # Business logic
        if any(word in prompt for word in ["workflow", "approval", "business_rules"]):
            factors["business_logic"] = 1
        
        # Edge cases
        total_edge_cases = edge_case_analysis.get("total_edge_cases", 0)
        if total_edge_cases > 5:
            factors["edge_cases"] = 2
        elif total_edge_cases > 2:
            factors["edge_cases"] = 1
        
        return factors
    
    def _calculate_base_complexity_score(self, factors: Dict[str, Any]) -> float:
        """Calculate base complexity score"""
        total_factors = sum(factors.values())
        return min(total_factors * 0.5, 3.0)
    
    def _calculate_edge_case_adjustment(self, edge_case_analysis: Dict) -> float:
        """Calculate edge case adjustment"""
        critical_edge_cases = len(edge_case_analysis.get("critical_edge_cases", []))
        return min(critical_edge_cases * 0.2, 1.0)
    
    def _determine_complexity_level(self, score: float) -> str:
        """Determine complexity level"""
        if score <= 1:
            return "simple"
        elif score <= 2:
            return "moderate"
        elif score <= 3:
            return "complex"
        else:
            return "expert"
    
    def _assess_technical_risks(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> List[str]:
        """Assess technical risks"""
        risks = []
        
        if any(word in prompt for word in ["performance", "scalability"]):
            risks.append("Performance bottlenecks under load")
        
        if any(word in prompt for word in ["security", "privacy"]):
            risks.append("Security vulnerabilities")
        
        if edge_case_analysis.get("total_edge_cases", 0) > 5:
            risks.append("Complex edge case handling")
        
        return risks
    
    def _assess_business_risks(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> List[str]:
        """Assess business risks"""
        risks = []
        
        if feature_analysis.get("user_impact") == "high":
            risks.append("High user adoption risk")
        
        if any(word in prompt for word in ["compliance", "regulatory"]):
            risks.append("Regulatory compliance risk")
        
        return risks
    
    def _assess_operational_risks(self, prompt: str, feature_analysis: Dict, edge_case_analysis: Dict) -> List[str]:
        """Assess operational risks"""
        risks = []
        
        if feature_analysis.get("feature_type") in ["dispute_management", "payment_processing"]:
            risks.append("High operational complexity")
        
        if edge_case_analysis.get("total_edge_cases", 0) > 3:
            risks.append("Increased support burden")
        
        return risks
    
    def _calculate_overall_risk_level(self, technical_risks: List[str], business_risks: List[str], operational_risks: List[str]) -> str:
        """Calculate overall risk level"""
        total_risks = len(technical_risks) + len(business_risks) + len(operational_risks)
        
        if total_risks >= 5:
            return "high"
        elif total_risks >= 3:
            return "medium"
        else:
            return "low"
    
    def _generate_risk_mitigation_strategies(self, risk_level: str) -> List[str]:
        """Generate risk mitigation strategies"""
        strategies = []
        
        if risk_level == "high":
            strategies.extend([
                "Implement comprehensive testing strategy",
                "Add monitoring and alerting",
                "Plan for gradual rollout",
                "Prepare rollback procedures"
            ])
        elif risk_level == "medium":
            strategies.extend([
                "Add unit and integration tests",
                "Implement error handling",
                "Plan for user feedback collection"
            ])
        else:
            strategies.append("Standard development practices")
        
        return strategies
    
    def _format_requirements(self, requirements: List[str]) -> str:
        """Format requirements for output"""
        if not requirements:
            return "No specific requirements identified"
        
        return "\n".join([f"• {req.replace('_', ' ').title()}" for req in requirements])
    
    def _format_edge_cases(self, edge_case_categories: Dict) -> str:
        """Format edge cases for output"""
        if not edge_case_categories:
            return "No edge cases identified"
        
        formatted = []
        for category, cases in edge_case_categories.items():
            formatted.append(f"**{category.title()}:** {', '.join(cases)}")
        
        return "\n".join(formatted)
    
    def _format_critical_edge_cases(self, critical_cases: List[str]) -> str:
        """Format critical edge cases for output"""
        if not critical_cases:
            return "No critical edge cases identified"
        
        return "\n".join([f"• {case.replace('_', ' ').title()}" for case in critical_cases])
    
    def _format_complexity_factors(self, factors: Dict) -> str:
        """Format complexity factors for output"""
        if not factors:
            return "No complexity factors identified"
        
        formatted = []
        for factor, value in factors.items():
            if value > 0:
                formatted.append(f"• {factor.replace('_', ' ').title()}: {value}")
        
        return "\n".join(formatted)
    
    def _format_risks(self, risks: List[str]) -> str:
        """Format risks for output"""
        if not risks:
            return "No risks identified"
        
        return "\n".join([f"• {risk}" for risk in risks])
    
    def _format_mitigation_strategies(self, strategies: List[str]) -> str:
        """Format mitigation strategies for output"""
        if not strategies:
            return "No mitigation strategies needed"
        
        return "\n".join([f"• {strategy}" for strategy in strategies])
    
    def _calculate_confidence(self, feature_analysis: Dict, viability_assessment: Dict, complexity_assessment: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Boost for clear feature type
        if feature_analysis.get("feature_type") != "general_feature":
            base_confidence += 0.05
        
        # Boost for good viability score
        viability_score = viability_assessment.get("overall_score", 0.0)
        if viability_score > 0.7:
            base_confidence += 0.05
        
        # Boost for reasonable complexity
        complexity_score = complexity_assessment.get("score", 0.0)
        if 1.0 <= complexity_score <= 3.0:
            base_confidence += 0.05
        
        return min(base_confidence, 0.95)
