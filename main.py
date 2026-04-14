import json
import pandas as pd
import os
from datetime import datetime

def generate_benchmark_csv(input_file: str = "data.json", 
                           output_file: str = None):
    """
    Converts the AGI benchmark JSON file into a clean, well-structured CSV 
    ready for Kaggle Measuring AGI submission.
    """
    try:
        
        if not os.path.exists(input_file):
            print(f"❌ Error: File '{input_file}' not found!")
            return None

        # Load the JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Support both single object and list of objects
        if isinstance(data, dict):
            data = [data]

        rows = []
        for item in data:
            theory = item.get('theory_levels', {})

            row = {
                "id": item.get("id"),
                "title": item.get("title"),
                "track": item.get("track"),
                "difficulty_tier": item.get("difficulty_tier", "Expert / AGI-Boundary"),
                
                # Main content
                "scenario": item.get("scenario"),
                "intuitive": theory.get("intuitive"),
                "technical": theory.get("technical"),
                "strategic": theory.get("strategic"),
                
                # Additional fields
                "solution": item.get("solution"),
                "counterfactual_check": item.get("counterfactual_check"),
                "trap": item.get("trap"),
                
                # Complex fields saved as JSON strings
                "parameters": json.dumps(item.get("parameters", {}), ensure_ascii=False),
                "evaluator_note-expert": json.dumps(item.get("evaluator_logic", {}), ensure_ascii=False),
                
                # Metadata
                "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            rows.append(row)

        # Create DataFrame
        df = pd.DataFrame(rows)

        # Generate output filename if not provided
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            output_file = f"agi_benchmark_20260414-081355.csv"

        # Export to CSV
        df.to_csv(output_file, index=False, encoding='utf-8')

        print(f"\n✅ SUCCESS - Benchmark generated successfully!")
        print(f"   Scenarios processed : {len(df)}")
        print(f"   Output file         : {output_file}")
        print(f"   Columns             : {list(df.columns)}")

        # Show preview of first 2 rows
        print("\n--- Preview of first 3 scenarios ---")
        print(df.head(3)[['id', 'title', 'track', 'difficulty_tier', 'solution']])

        return df

    except Exception as e:
        print(f"❌ Error generating CSV: {e}")
        return None


if __name__ == "__main__":
    # You can change the input filename here if needed
    generate_benchmark_csv("data.json")
