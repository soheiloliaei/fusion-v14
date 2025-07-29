#!/usr/bin/env python3
"""
Fusion v14 - CLI Runner
Programmable agent OS for design and evaluation
"""

import argparse
import asyncio
import sys

from agents.vp_design_agent import VPDesignAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.creative_director_agent import CreativeDirectorAgent
from agents.prompt_master_agent import PromptMasterAgent
from core.execution_orchestrator_v14 import ExecutionOrchestrator

print("🧠 DEBUG: fusion.py top-level code executed")

def main():
    parser = argparse.ArgumentParser(description="Fusion v14 CLI")
    subparsers = parser.add_subparsers(dest="command")

    # 'run' command: single agent
    run_parser = subparsers.add_parser("run", help="Run a single agent")
    run_parser.add_argument("agent", type=str, help="Agent name (e.g., vp_design)")
    run_parser.add_argument("input", nargs=argparse.REMAINDER, help="Input prompt")

    # 'pipeline' command: full pipeline execution
    pipeline_parser = subparsers.add_parser("pipeline", help="Run pipeline with prompt")
    pipeline_parser.add_argument("input", nargs=argparse.REMAINDER, help="Pipeline input")

    # Parse args
    args = parser.parse_args()
    print(f"🛠 DEBUG: Parsed args = {args}")

    if args.command == "run":
        if not args.input:
            print("❌ Error: 'run' command requires input")
            sys.exit(1)

        input_text = " ".join(args.input)
        print(f"�� Running agent '{args.agent}' on input: {input_text}")

        # Dynamic agent loading
        agent_map = {
            "vp_design": VPDesignAgent,
            "evaluator": EvaluatorAgent,
            "creative_director": CreativeDirectorAgent,
            "prompt_master": PromptMasterAgent,
            "design_technologist": "DesignTechnologistAgent",  # Placeholder
            "product_navigator": "ProductNavigatorAgent",  # Placeholder
            "strategy_pilot": "StrategyPilotAgent",  # Placeholder
            "vp_of_design": "VPOfDesignAgent",  # Placeholder
            "vp_of_product": "VPOfProductAgent"  # Placeholder
        }
        
        if args.agent in agent_map:
            if args.agent in ["vp_design", "evaluator", "creative_director", "prompt_master"]:
                # Working agents
                agent_class = agent_map[args.agent]
                agent = agent_class()
                output = asyncio.run(agent.run_async(input_text, {}))
                print(f"🎨 Output from {args.agent}:\n{output}")
            else:
                # Placeholder agents (need implementation)
                print(f"⚠️ Agent '{args.agent}' is available but not yet implemented")
                print(f"Available working agents: vp_design, evaluator, creative_director, prompt_master")
                print(f"Available placeholder agents: {', '.join([k for k in agent_map.keys() if k not in ['vp_design', 'evaluator']])}")
                sys.exit(1)
        else:
            print(f"❌ Error: Unknown agent '{args.agent}'")
            print(f"Available agents: {', '.join(agent_map.keys())}")
            sys.exit(1)

    elif args.command == "pipeline":
        if not args.input:
            print("❌ Error: 'pipeline' command requires input")
            sys.exit(1)

        input_text = " ".join(args.input)
        print(f"⚙️ Running pipeline on: {input_text}")

        from core.fusion_context import FusionContext
        context = FusionContext({})
        orchestrator = ExecutionOrchestrator(context)
        
        # Register agents and tools
        from tools.ux_audit_tool import UXAuditTool
        from tools.trust_explainer_tool import TrustExplainerTool
        
        # Register working agents
        orchestrator.register_agent("vp_design", VPDesignAgent())
        orchestrator.register_agent("evaluator", EvaluatorAgent())
        
        # Register tools
        orchestrator.register_tool("ux_audit", UXAuditTool())
        orchestrator.register_tool("trust_explainer", TrustExplainerTool())
        
        print(f"✅ Registered agents: vp_design, evaluator")
        print(f"✅ Registered tools: ux_audit, trust_explainer")
        print(f"📋 Available agents (not yet implemented): creative_director, prompt_master, design_technologist, product_navigator, strategy_pilot, vp_of_design, vp_of_product")
        
        output = asyncio.run(orchestrator.execute_pipeline(input_text))
        print(f"🧩 Pipeline Output:\n{output}")

    else:
        print("❌ Error: Unknown command. Use 'run' or 'pipeline'")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    print("🧠 DEBUG: Entering main()")
    main()
