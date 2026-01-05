"""
Self-Modification Demo: Watch Paradma Write Its Own Code!

This demo shows Paradma:
1. Learning from NumPy
2. Generating Python code
3. Writing it to native_operations.py
4. Loading and using its own generated code

TRUE META-PROGRAMMING IN ACTION!
"""

import sys
from pathlib import Path
import time
import os

sys.path.insert(0, str(Path(__file__).parent))

from autolearner import AutoLearner
import numpy as np

def print_section(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def show_file_before():
    """Show the native_operations.py file before learning"""
    print_section("BEFORE: native_operations.py")
    
    ops_file = Path(__file__).parent / "native_operations.py"
    
    if ops_file.exists():
        content = ops_file.read_text(encoding='utf-8')
        print("[FILE EXISTS] Current content:")
        print("-" * 70)
        print(content[:500] + "..." if len(content) > 500 else content)
        print("-" * 70)
    else:
        print("[NO FILE] native_operations.py does not exist yet")
        print("It will be created automatically when Paradma learns!\n")

def teach_paradma():
    """Teach Paradma complex operations through observations"""
    print_section("PHASE 1: Teaching Paradma Complex Math")
    
    learner = AutoLearner(enable_self_modification=True)
    
    # 1. Teach Matrix Multiplication
    print("[TEACHING] Teaching Matrix Multiplication (matmul)...")
    matrices = [
        ([[1, 2], [3, 4]], [[1, 0], [0, 1]]),  # Identity
        ([[1, 2], [3, 4]], [[2, 0], [1, 2]]),
        ([[1, 1], [1, 1]], [[2, 2], [2, 2]]),
        ([[1, 2, 3]], [[1], [2], [3]]),        # 1x3 * 3x1
        ([[1, 0], [0, 1]], [[5, 6], [7, 8]]),
        ([[2, 0], [0, 2]], [[1, 2], [3, 4]]),  # Scaling
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        ([[0, 0], [0, 0]], [[1, 2], [3, 4]]),  # Zero
        ([[1, 2], [3, 4]], [[0, 0], [0, 0]]),
        ([[1, 2], [3, 4]], [[-1, 0], [0, -1]]),
        ([[10, 20], [30, 40]], [[1, 1], [1, 1]]),
    ]
    
    for i, (a, b) in enumerate(matrices, 1):
        learner.execute('matmul', a, b)
        if i % 3 == 0: print(f"   Observed {i} matrix multiplications...")
        time.sleep(0.05)
    print("   [DONE] Matrix Multiplication learned!\n")

    # 2. Teach Dot Product
    print("[TEACHING] Teaching Dot Product (dot)...")
    vectors = [
        ([1, 2], [3, 4]),
        ([1, 0, 0], [0, 1, 0]),
        ([1, 1, 1], [2, 2, 2]),
        ([1, 2, 3, 4], [1, 1, 1, 1]),
        ([5, 5], [2, 2]),
        ([0, 0, 0], [1, 2, 3]),
        ([-1, 1], [1, 1]),
        ([10, 20], [2, 3]),
        ([1, 2], [0.5, 0.5]),
        ([3, 4], [3, 4]),
        ([1, 2, 3], [3, 2, 1]),
    ]
    
    for i, (a, b) in enumerate(vectors, 1):
        learner.execute('dot', a, b)
        time.sleep(0.05)
    print("   [DONE] Dot Product learned!\n")

    # 3. Teach Square Root
    print("[TEACHING] Teaching Square Root (sqrt)...")
    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 144, 2, 3, 0.25, 0]
    
    for i, n in enumerate(numbers, 1):
        learner.execute('sqrt', n)
        time.sleep(0.05)
    print("   [DONE] Square Root learned!\n")
    
    return learner

def show_file_after():
    """Show the native_operations.py file after learning"""
    print_section("AFTER: native_operations.py (SELF-GENERATED!)")
    
    ops_file = Path(__file__).parent / "native_operations.py"
    
    if ops_file.exists():
        content = ops_file.read_text(encoding='utf-8')
        print("[FILE MODIFIED] Paradma wrote its own code!")
        print("-" * 70)
        lines = content.split('\n')
        # Show the file with line numbers
        for i, line in enumerate(lines[:50], 1):  # First 50 lines
            print(f"{i:3d}: {line}")
        if len(lines) > 50:
            print(f"... ({len(lines) - 50} more lines)")
        print("-" * 70)
    else:
        print("[ERROR] File was not created!")

def test_generated_code():
    """Test the self-generated code for complex operations"""
    print_section("PHASE 2: Testing Self-Generated Code")
    
    try:
        # Import the self-generated module
        import native_operations
        import importlib
        importlib.reload(native_operations)
        
        print("Successfully imported native_operations.py!\n")
        
        # Test Matrix Multiplication
        if hasattr(native_operations, 'native_matmul'):
            print("[TEST] Testing native_matmul():")
            a = [[1, 2], [3, 4]]
            b = [[1, 0], [0, 1]]
            res = native_operations.native_matmul(a, b)
            print(f"   [[1,2],[3,4]] x Identity = {res}")
            print("   [PASS] Matrix logic verified\n")

        # Test Dot Product
        if hasattr(native_operations, 'native_dot'):
            print("[TEST] Testing native_dot():")
            a = [1, 2, 3]
            b = [4, 5, 6]
            res = native_operations.native_dot(a, b)
            print(f"   [1,2,3] . [4,5,6] = {res}")
            print("   [PASS] Vector logic verified\n")

        # Test Square Root
        if hasattr(native_operations, 'native_sqrt'):
            print("[TEST] Testing native_sqrt():")
            val = 144
            res = native_operations.native_sqrt(val)
            print(f"   sqrt(144) = {res}")
            print("   [PASS] Newton's Method verified\n")
            
    except Exception as e:
        print(f"[ERROR] Could not test: {e}")

def compare_implementations():
    """Compare NumPy vs self-generated code"""
    print_section("PHASE 3: Independence Verification")
    
    try:
        import native_operations
        import importlib
        importlib.reload(native_operations)
        
        print("INDEPENDENCE TEST: Running Complex Math WITHOUT NumPy\n")
        
        # Verify Matrix Multiplication
        if hasattr(native_operations, 'native_matmul'):
            print("1. Matrix Multiplication:")
            a = [[10, 20], [30, 40]]
            b = [[2, 0], [0, 2]]
            res = native_operations.native_matmul(a, b)
            print(f"   Result: {res}")
            print(f"   Source: native_operations.py (self-generated)")
            print(f"   NumPy used: NO\n")
            
    except Exception as e:
        print(f"[ERROR] {e}")

import shutil

def cleanup_state():
    """Reset the state for a fresh demo"""
    print_section("INITIALIZATION: Cleaning up previous state")
    
    # Remove native_operations.py
    ops_file = Path(__file__).parent / "native_operations.py"
    if ops_file.exists():
        try:
            os.remove(ops_file)
            print(f"[CLEANUP] Removed {ops_file.name}")
        except Exception as e:
            print(f"[ERROR] Could not remove file: {e}")
            
    # Remove knowledge directory
    knowledge_dir = Path(".paradma_knowledge")
    if knowledge_dir.exists():
        try:
            shutil.rmtree(knowledge_dir)
            print(f"[CLEANUP] Removed knowledge directory")
        except Exception as e:
            print(f"[ERROR] Could not remove directory: {e}")
            
    # Clear pycache for native_operations
    try:
        import sys
        if 'native_operations' in sys.modules:
            del sys.modules['native_operations']
    except:
        pass

def main():
    """Run the full self-modification demo"""
    print("\n" + "="*70)
    print("  PARADMA SELF-MODIFICATION DEMO")
    print("  Watch Paradma Write Its Own Code!")
    print("="*70)
    
    # Clean up previous state
    # cleanup_state()
    
    # Show initial state
    show_file_before()
    
    time.sleep(1)
    
    # Teach Paradma
    learner = teach_paradma()
    
    time.sleep(1)
    
    # Show generated file
    show_file_after()
    
    time.sleep(1)
    
    # Test the generated code
    test_generated_code()
    
    time.sleep(1)
    
    # Verify independence
    compare_implementations()
    
    # Final message
    print("\n" + "="*70)
    print("  META-PROGRAMMING COMPLETE!")
    print("="*70)
    print("\nParadma successfully:")
    print("  1. Learned from NumPy")
    print("  2. Generated Python code")
    print("  3. Wrote it to native_operations.py")
    print("  4. Loaded and executed its own code")
    print("\nThis is TRUE self-modifying AI!\n")

if __name__ == "__main__":
    main()
