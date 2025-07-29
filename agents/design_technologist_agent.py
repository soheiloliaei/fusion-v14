#!/usr/bin/env python3
"""
Design Technologist Agent - Fusion v14
Handles Figma-to-code fidelity, token extraction, Tailwind/React mapping
"""

import asyncio
import time
import logging
import re
from typing import Dict, Any, List, Optional
from datetime import datetime

class DesignTechnologistAgent:
    """
    Design Technologist Agent - Fusion v14
    Handles Figma-to-code fidelity, token extraction, Tailwind/React mapping
    """
    
    def __init__(self):
        self.logger = logging.getLogger("DesignTechnologistAgent")
        
        # Design token categories
        self.token_categories = {
            "colors": ["primary", "secondary", "accent", "neutral", "success", "warning", "error"],
            "typography": ["font_family", "font_size", "font_weight", "line_height", "letter_spacing"],
            "spacing": ["padding", "margin", "gap", "border_radius", "shadow"],
            "layout": ["width", "height", "flex", "grid", "position"],
            "interaction": ["hover", "focus", "active", "disabled", "transition"]
        }
        
        # Tailwind utility mappings
        self.tailwind_mappings = {
            "colors": {
                "primary": "bg-blue-500 text-white",
                "secondary": "bg-gray-500 text-white", 
                "accent": "bg-purple-500 text-white",
                "success": "bg-green-500 text-white",
                "warning": "bg-yellow-500 text-black",
                "error": "bg-red-500 text-white"
            },
            "spacing": {
                "xs": "p-1 m-1",
                "sm": "p-2 m-2", 
                "md": "p-4 m-4",
                "lg": "p-6 m-6",
                "xl": "p-8 m-8"
            },
            "typography": {
                "heading": "text-2xl font-bold",
                "subheading": "text-xl font-semibold",
                "body": "text-base font-normal",
                "caption": "text-sm font-light"
            }
        }
        
        # Component complexity levels
        self.complexity_levels = {
            "simple": {"score": 1, "description": "Basic layout with standard components"},
            "moderate": {"score": 2, "description": "Interactive elements with state management"},
            "complex": {"score": 3, "description": "Advanced interactions with custom logic"},
            "expert": {"score": 4, "description": "Highly customized with complex animations"}
        }
        
        # Accessibility requirements
        self.accessibility_requirements = [
            "semantic_html",
            "aria_labels", 
            "keyboard_navigation",
            "color_contrast",
            "focus_indicators",
            "screen_reader_support"
        ]
        
    async def run_async(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main async execution method for Design Technologist Agent
        """
        start_time = time.time()
        self.logger.info("Design Technologist Agent starting analysis")
        
        try:
            # Analyze design requirements
            design_analysis = await self._analyze_design_requirements(prompt)
            
            # Extract design tokens
            token_extraction = await self._extract_design_tokens(prompt, design_analysis)
            
            # Generate Tailwind/React mapping
            code_mapping = await self._generate_code_mapping(prompt, token_extraction)
            
            # Assess component complexity
            complexity_assessment = await self._assess_component_complexity(prompt, design_analysis)
            
            # Generate accessibility recommendations
            accessibility_recommendations = await self._generate_accessibility_recommendations(prompt, design_analysis)
            
            # Create enhanced output
            enhanced_output = await self._create_enhanced_output(prompt, design_analysis, token_extraction, code_mapping, complexity_assessment, accessibility_recommendations)
            
            execution_time = time.time() - start_time
            confidence = self._calculate_confidence(design_analysis, token_extraction, complexity_assessment)
            
            self.logger.info(f"Design Technologist Agent completed in {execution_time:.2f}s")
            
            return {
                "output": enhanced_output,
                "enhanced_output": enhanced_output,
                "confidence": confidence,
                "design_analysis": design_analysis,
                "token_extraction": token_extraction,
                "code_mapping": code_mapping,
                "complexity_assessment": complexity_assessment,
                "accessibility_recommendations": accessibility_recommendations,
                "execution_time": execution_time,
                "shared_state": {
                    "component_type": design_analysis.get("component_type"),
                    "complexity_level": complexity_assessment.get("level"),
                    "token_count": len(token_extraction.get("extracted_tokens", [])),
                    "accessibility_score": accessibility_recommendations.get("score"),
                    "analysis_timestamp": datetime.now().timestamp()
                }
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Design Technologist Agent failed: {e}")
            return {
                "error": str(e),
                "confidence": 0.0,
                "execution_time": execution_time
            }
    
    async def _analyze_design_requirements(self, prompt: str) -> Dict[str, Any]:
        """Analyze design requirements from prompt"""
        
        prompt_lower = prompt.lower()
        
        # Detect component type
        component_type = self._detect_component_type(prompt_lower)
        
        # Identify design patterns
        design_patterns = self._identify_design_patterns(prompt_lower)
        
        # Extract technical requirements
        technical_requirements = self._extract_technical_requirements(prompt_lower)
        
        return {
            "component_type": component_type,
            "design_patterns": design_patterns,
            "technical_requirements": technical_requirements,
            "framework_preferences": self._detect_framework_preferences(prompt_lower)
        }
    
    async def _extract_design_tokens(self, prompt: str, design_analysis: Dict) -> Dict[str, Any]:
        """Extract design tokens from prompt and analysis"""
        
        extracted_tokens = []
        token_categories = {}
        
        # Extract color tokens
        color_tokens = self._extract_color_tokens(prompt)
        if color_tokens:
            token_categories["colors"] = color_tokens
            extracted_tokens.extend(color_tokens)
        
        # Extract typography tokens
        typography_tokens = self._extract_typography_tokens(prompt)
        if typography_tokens:
            token_categories["typography"] = typography_tokens
            extracted_tokens.extend(typography_tokens)
        
        # Extract spacing tokens
        spacing_tokens = self._extract_spacing_tokens(prompt)
        if spacing_tokens:
            token_categories["spacing"] = spacing_tokens
            extracted_tokens.extend(spacing_tokens)
        
        # Extract layout tokens
        layout_tokens = self._extract_layout_tokens(prompt)
        if layout_tokens:
            token_categories["layout"] = layout_tokens
            extracted_tokens.extend(layout_tokens)
        
        return {
            "extracted_tokens": extracted_tokens,
            "token_categories": token_categories,
            "token_count": len(extracted_tokens),
            "coverage_score": self._calculate_token_coverage(extracted_tokens)
        }
    
    async def _generate_code_mapping(self, prompt: str, token_extraction: Dict) -> Dict[str, Any]:
        """Generate Tailwind/React code mapping"""
        
        # Generate Tailwind utilities
        tailwind_utilities = self._generate_tailwind_utilities(token_extraction)
        
        # Generate React component structure
        react_structure = self._generate_react_structure(prompt, token_extraction)
        
        # Generate CSS custom properties
        css_properties = self._generate_css_properties(token_extraction)
        
        return {
            "tailwind_utilities": tailwind_utilities,
            "react_structure": react_structure,
            "css_properties": css_properties,
            "implementation_notes": self._generate_implementation_notes(prompt, token_extraction)
        }
    
    async def _assess_component_complexity(self, prompt: str, design_analysis: Dict) -> Dict[str, Any]:
        """Assess component complexity"""
        
        complexity_factors = self._analyze_complexity_factors(prompt, design_analysis)
        complexity_score = self._calculate_complexity_score(complexity_factors)
        complexity_level = self._determine_complexity_level(complexity_score)
        
        return {
            "level": complexity_level,
            "score": complexity_score,
            "factors": complexity_factors,
            "description": self.complexity_levels[complexity_level]["description"],
            "development_effort": self._estimate_development_effort(complexity_score)
        }
    
    async def _generate_accessibility_recommendations(self, prompt: str, design_analysis: Dict) -> Dict[str, Any]:
        """Generate accessibility recommendations"""
        
        # Identify accessibility requirements
        accessibility_requirements = self._identify_accessibility_requirements(prompt, design_analysis)
        
        # Generate implementation guidelines
        implementation_guidelines = self._generate_accessibility_guidelines(accessibility_requirements)
        
        # Calculate accessibility score
        accessibility_score = self._calculate_accessibility_score(accessibility_requirements)
        
        return {
            "requirements": accessibility_requirements,
            "guidelines": implementation_guidelines,
            "score": accessibility_score,
            "priority_items": self._identify_priority_accessibility_items(accessibility_requirements)
        }
    
    async def _create_enhanced_output(self, prompt: str, design_analysis: Dict, token_extraction: Dict, code_mapping: Dict, complexity_assessment: Dict, accessibility_recommendations: Dict) -> str:
        """Create enhanced output with technical analysis"""
        
        return f"""# Design Technologist Analysis & Implementation

## Original Request
{prompt}

## Design Analysis

### Component Type
**Type:** {design_analysis.get('component_type', 'unknown')}
**Patterns:** {', '.join(design_analysis.get('design_patterns', ['None detected']))}
**Framework:** {design_analysis.get('framework_preferences', 'Tailwind CSS')}

## Token Extraction

### Extracted Tokens ({token_extraction.get('token_count', 0)} total)
{self._format_token_categories(token_extraction.get('token_categories', {}))}

### Coverage Score
**Score:** {token_extraction.get('coverage_score', 0):.2f}/1.00

## Code Implementation

### Tailwind Utilities
```
{code_mapping.get('tailwind_utilities', 'No utilities generated')}
```

### React Component Structure
```jsx
{code_mapping.get('react_structure', '// Component structure not generated')}
```

### CSS Custom Properties
```css
{code_mapping.get('css_properties', '/* No custom properties */')}
```

## Complexity Assessment

### Level: {complexity_assessment.get('level', 'unknown').upper()}
**Score:** {complexity_assessment.get('score', 0):.1f}/4.0
**Description:** {complexity_assessment.get('description', 'No description available')}
**Development Effort:** {complexity_assessment.get('development_effort', 'Unknown')}

## Accessibility Recommendations

### Requirements
{self._format_accessibility_requirements(accessibility_recommendations.get('requirements', []))}

### Implementation Guidelines
{self._format_implementation_guidelines(accessibility_recommendations.get('guidelines', []))}

### Accessibility Score
**Score:** {accessibility_recommendations.get('score', 0):.2f}/1.00

## Implementation Notes
{code_mapping.get('implementation_notes', 'No specific notes')}

## Design Technologist Confidence
**Score:** {self._calculate_confidence(design_analysis, token_extraction, complexity_assessment):.2f}/1.00

*Generated by Fusion v14 Design Technologist Agent*"""
    
    def _detect_component_type(self, prompt: str) -> str:
        """Detect component type from prompt"""
        if "button" in prompt or "btn" in prompt:
            return "button"
        elif "card" in prompt or "tile" in prompt:
            return "card"
        elif "form" in prompt or "input" in prompt:
            return "form"
        elif "modal" in prompt or "dialog" in prompt:
            return "modal"
        elif "navigation" in prompt or "nav" in prompt:
            return "navigation"
        elif "dashboard" in prompt or "layout" in prompt:
            return "dashboard"
        else:
            return "custom"
    
    def _identify_design_patterns(self, prompt: str) -> List[str]:
        """Identify design patterns in prompt"""
        patterns = []
        
        if "responsive" in prompt or "mobile" in prompt:
            patterns.append("responsive_design")
        
        if "dark" in prompt or "theme" in prompt:
            patterns.append("theme_support")
        
        if "animation" in prompt or "transition" in prompt:
            patterns.append("animations")
        
        if "grid" in prompt or "flex" in prompt:
            patterns.append("layout_system")
        
        return patterns
    
    def _extract_technical_requirements(self, prompt: str) -> List[str]:
        """Extract technical requirements"""
        requirements = []
        
        if "tailwind" in prompt:
            requirements.append("tailwind_css")
        
        if "react" in prompt:
            requirements.append("react_components")
        
        if "accessibility" in prompt or "a11y" in prompt:
            requirements.append("accessibility")
        
        if "responsive" in prompt:
            requirements.append("responsive_design")
        
        return requirements
    
    def _detect_framework_preferences(self, prompt: str) -> str:
        """Detect framework preferences"""
        if "tailwind" in prompt:
            return "Tailwind CSS"
        elif "react" in prompt:
            return "React"
        elif "vue" in prompt:
            return "Vue.js"
        else:
            return "Tailwind CSS"  # Default
    
    def _extract_color_tokens(self, prompt: str) -> List[str]:
        """Extract color tokens from prompt"""
        colors = []
        
        # Extract color names
        color_keywords = ["blue", "red", "green", "yellow", "purple", "gray", "white", "black"]
        for color in color_keywords:
            if color in prompt:
                colors.append(f"color_{color}")
        
        # Extract semantic colors
        semantic_colors = ["primary", "secondary", "accent", "success", "warning", "error"]
        for semantic in semantic_colors:
            if semantic in prompt:
                colors.append(f"color_{semantic}")
        
        return colors
    
    def _extract_typography_tokens(self, prompt: str) -> List[str]:
        """Extract typography tokens from prompt"""
        typography = []
        
        # Extract font sizes
        font_sizes = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl"]
        for size in font_sizes:
            if size in prompt:
                typography.append(f"font_size_{size}")
        
        # Extract font weights
        font_weights = ["light", "normal", "medium", "semibold", "bold"]
        for weight in font_weights:
            if weight in prompt:
                typography.append(f"font_weight_{weight}")
        
        return typography
    
    def _extract_spacing_tokens(self, prompt: str) -> List[str]:
        """Extract spacing tokens from prompt"""
        spacing = []
        
        # Extract spacing values
        spacing_values = ["xs", "sm", "md", "lg", "xl"]
        for value in spacing_values:
            if value in prompt:
                spacing.append(f"spacing_{value}")
        
        return spacing
    
    def _extract_layout_tokens(self, prompt: str) -> List[str]:
        """Extract layout tokens from prompt"""
        layout = []
        
        # Extract layout patterns
        layout_patterns = ["flex", "grid", "block", "inline"]
        for pattern in layout_patterns:
            if pattern in prompt:
                layout.append(f"layout_{pattern}")
        
        return layout
    
    def _calculate_token_coverage(self, tokens: List[str]) -> float:
        """Calculate token coverage score"""
        if not tokens:
            return 0.0
        
        # Simple coverage calculation
        base_coverage = min(len(tokens) / 10.0, 1.0)
        return base_coverage
    
    def _generate_tailwind_utilities(self, token_extraction: Dict) -> str:
        """Generate Tailwind utilities from tokens"""
        utilities = []
        token_categories = token_extraction.get("token_categories", {})
        
        # Generate color utilities
        if "colors" in token_categories:
            for color in token_categories["colors"]:
                if "primary" in color:
                    utilities.append("bg-blue-500 text-white")
                elif "secondary" in color:
                    utilities.append("bg-gray-500 text-white")
                elif "success" in color:
                    utilities.append("bg-green-500 text-white")
                elif "warning" in color:
                    utilities.append("bg-yellow-500 text-black")
                elif "error" in color:
                    utilities.append("bg-red-500 text-white")
        
        # Generate spacing utilities
        if "spacing" in token_categories:
            utilities.append("p-4 m-2 rounded-lg")
        
        # Generate typography utilities
        if "typography" in token_categories:
            utilities.append("text-base font-medium")
        
        return " ".join(utilities) if utilities else "p-4 bg-white rounded-lg"
    
    def _generate_react_structure(self, prompt: str, token_extraction: Dict) -> str:
        """Generate React component structure"""
        component_type = self._detect_component_type(prompt.lower())
        
        if component_type == "button":
            return """export default function Button({ children, ...props }) {
  return (
    <button 
      className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
      {...props}
    >
      {children}
    </button>
  );
}"""
        elif component_type == "card":
            return """export default function Card({ children, ...props }) {
  return (
    <div 
      className="p-6 bg-white rounded-lg shadow-md border border-gray-200"
      {...props}
    >
      {children}
    </div>
  );
}"""
        else:
            return """export default function Component({ children, ...props }) {
  return (
    <div className="p-4 bg-white rounded-lg" {...props}>
      {children}
    </div>
  );
}"""
    
    def _generate_css_properties(self, token_extraction: Dict) -> str:
        """Generate CSS custom properties"""
        properties = []
        token_categories = token_extraction.get("token_categories", {})
        
        if "colors" in token_categories:
            properties.append("  --color-primary: #3b82f6;")
            properties.append("  --color-secondary: #6b7280;")
        
        if "spacing" in token_categories:
            properties.append("  --spacing-base: 1rem;")
            properties.append("  --spacing-lg: 1.5rem;")
        
        return "/* CSS Custom Properties */\n:root {\n" + "\n".join(properties) + "\n}" if properties else "/* No custom properties needed */"
    
    def _generate_implementation_notes(self, prompt: str, token_extraction: Dict) -> str:
        """Generate implementation notes"""
        notes = []
        
        if token_extraction.get("token_count", 0) > 5:
            notes.append("• Consider creating a design token system for consistency")
        
        if "accessibility" in prompt.lower():
            notes.append("• Ensure proper ARIA labels and keyboard navigation")
        
        if "responsive" in prompt.lower():
            notes.append("• Test across different screen sizes and devices")
        
        return "\n".join(notes) if notes else "• Follow standard implementation practices"
    
    def _analyze_complexity_factors(self, prompt: str, design_analysis: Dict) -> Dict[str, Any]:
        """Analyze complexity factors"""
        factors = {
            "interactions": 0,
            "animations": 0,
            "state_management": 0,
            "accessibility": 0,
            "responsive_design": 0
        }
        
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ["hover", "click", "interactive"]):
            factors["interactions"] = 1
        
        if any(word in prompt_lower for word in ["animation", "transition", "motion"]):
            factors["animations"] = 1
        
        if any(word in prompt_lower for word in ["state", "form", "validation"]):
            factors["state_management"] = 1
        
        if any(word in prompt_lower for word in ["accessibility", "a11y", "aria"]):
            factors["accessibility"] = 1
        
        if any(word in prompt_lower for word in ["responsive", "mobile", "tablet"]):
            factors["responsive_design"] = 1
        
        return factors
    
    def _calculate_complexity_score(self, factors: Dict[str, Any]) -> float:
        """Calculate complexity score"""
        total_factors = sum(factors.values())
        return min(total_factors * 0.5, 3.0)
    
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
    
    def _estimate_development_effort(self, complexity_score: float) -> str:
        """Estimate development effort"""
        if complexity_score <= 1:
            return "1-2 hours"
        elif complexity_score <= 2:
            return "2-4 hours"
        elif complexity_score <= 3:
            return "4-8 hours"
        else:
            return "8+ hours"
    
    def _identify_accessibility_requirements(self, prompt: str, design_analysis: Dict) -> List[str]:
        """Identify accessibility requirements"""
        requirements = []
        prompt_lower = prompt.lower()
        
        if "accessibility" in prompt_lower or "a11y" in prompt_lower:
            requirements.extend(self.accessibility_requirements)
        else:
            # Basic accessibility for all components
            requirements.extend(["semantic_html", "aria_labels", "keyboard_navigation"])
        
        return requirements
    
    def _generate_accessibility_guidelines(self, requirements: List[str]) -> List[str]:
        """Generate accessibility implementation guidelines"""
        guidelines = []
        
        for requirement in requirements:
            if requirement == "semantic_html":
                guidelines.append("• Use semantic HTML elements (button, nav, main, etc.)")
            elif requirement == "aria_labels":
                guidelines.append("• Add appropriate ARIA labels and roles")
            elif requirement == "keyboard_navigation":
                guidelines.append("• Ensure keyboard navigation works properly")
            elif requirement == "color_contrast":
                guidelines.append("• Maintain sufficient color contrast ratios")
            elif requirement == "focus_indicators":
                guidelines.append("• Provide visible focus indicators")
            elif requirement == "screen_reader_support":
                guidelines.append("• Test with screen readers")
        
        return guidelines
    
    def _calculate_accessibility_score(self, requirements: List[str]) -> float:
        """Calculate accessibility score"""
        if not requirements:
            return 0.0
        
        return min(len(requirements) / len(self.accessibility_requirements), 1.0)
    
    def _identify_priority_accessibility_items(self, requirements: List[str]) -> List[str]:
        """Identify priority accessibility items"""
        priority_items = []
        
        if "semantic_html" in requirements:
            priority_items.append("semantic_html")
        
        if "aria_labels" in requirements:
            priority_items.append("aria_labels")
        
        return priority_items[:3]  # Top 3 priorities
    
    def _format_token_categories(self, token_categories: Dict) -> str:
        """Format token categories for output"""
        if not token_categories:
            return "No tokens extracted"
        
        formatted = []
        for category, tokens in token_categories.items():
            formatted.append(f"**{category.title()}:** {', '.join(tokens)}")
        
        return "\n".join(formatted)
    
    def _format_accessibility_requirements(self, requirements: List[str]) -> str:
        """Format accessibility requirements for output"""
        if not requirements:
            return "No specific requirements"
        
        return "\n".join([f"• {req.replace('_', ' ').title()}" for req in requirements])
    
    def _format_implementation_guidelines(self, guidelines: List[str]) -> str:
        """Format implementation guidelines for output"""
        if not guidelines:
            return "No specific guidelines"
        
        return "\n".join(guidelines)
    
    def _calculate_confidence(self, design_analysis: Dict, token_extraction: Dict, complexity_assessment: Dict) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Boost for clear component type
        if design_analysis.get("component_type") != "unknown":
            base_confidence += 0.05
        
        # Boost for good token coverage
        coverage_score = token_extraction.get("coverage_score", 0.0)
        if coverage_score > 0.5:
            base_confidence += 0.05
        
        # Boost for reasonable complexity
        complexity_score = complexity_assessment.get("score", 0.0)
        if 1.0 <= complexity_score <= 3.0:
            base_confidence += 0.05
        
        return min(base_confidence, 0.95)
