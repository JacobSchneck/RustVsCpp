# Jacob Schneck
# CS 120
# Module Three: Open Ended Project

import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import sys

def main():
    cpp_file = "cpp_data.txt"
    rust_file = "rust_data.txt"

    cpp_read_file = []
    cpp_merge_sort = []
    cpp_binary_search = []

    rust_read_file = []
    rust_merge_sort = []
    rust_binary_search = []

    size = 50 
    # Runs when no args passed to python file
    if len(sys.argv) == 1:
        print("Run Cpp and Rust files with default compililation optimazations (as ns)")
        os.system("g++ main.cpp")
        os.system("RUSTFLAGS=-Awarnings cargo run --manifest-path rust_version/Cargo.toml")

        # compile and run 10 times 
        for _ in range(size):
            # run with normal debug build
            os.system("./a.out")
            os.system("./rust_version/target/debug/rust_version")

            # open cpp and rust files and store data
            with open(cpp_file) as cpp_reader: 
                cpp_data = cpp_reader.readlines()
                cpp_data = [int(line.rstrip()) for line in cpp_data]
                cpp_read_file.append(cpp_data[0])
                cpp_merge_sort.append(cpp_data[1])
                cpp_binary_search.append(cpp_data[2])

                

            with open(rust_file) as rust_reader:
                rust_data = rust_reader.readlines()
                rust_data = [int(line.rstrip()) for line in rust_data]
                rust_read_file.append(rust_data[0])
                rust_merge_sort.append(rust_data[1])
                rust_binary_search.append(rust_data[2])
            

        # graph and save into .png files
        X = np.arange(size)

        cpp_read_file_ave = sum(cpp_read_file)/(len(cpp_read_file))
        cpp_merge_sort_ave = sum(cpp_merge_sort)/(len(cpp_merge_sort))
        cpp_binary_search_ave = sum(cpp_binary_search)/(len(cpp_binary_search))

        rust_read_file_ave = sum(rust_read_file)/(len(rust_read_file))
        rust_merge_sort_ave = sum(rust_merge_sort)/(len(rust_merge_sort))
        rust_binary_search_ave = sum(rust_binary_search)/(len(rust_binary_search))

        plt.figure()
        plt.plot(X, cpp_read_file, 'ob', markerfacecolor='none')
        plt.plot(X, rust_read_file, 'sr', markerfacecolor='none')
        plt.plot(X, [cpp_read_file_ave for _ in X], '--b')
        plt.plot(X, [rust_read_file_ave for _ in X], '--r')
        plt.xlabel('x-axis')
        plt.ylabel('Runtime in nanoseconds')
        plt.title("Comparison of Rust vs Cpp in Reading from a File")
        plt.legend(['Cpp Data', 'Rust Data', 'Cpp Average', 'Rust Average'])
        plt.savefig("Non_Optimized_data_read_file.png")

        plt.figure()
        plt.plot(X, cpp_merge_sort, 'ob', markerfacecolor='none')
        plt.plot(X, rust_merge_sort, 'sr', markerfacecolor='none')
        plt.plot(X, [cpp_merge_sort_ave for _ in X], '--b')
        plt.plot(X, [rust_merge_sort_ave for _ in X], '--r')
        plt.xlabel('x-axis')
        plt.ylabel('Runtime in nanoseconds')
        plt.title("Comparison of Rust vs Cpp in Merge Sort")
        plt.legend(['Cpp Data', 'Rust Data', 'Cpp Average', 'Rust Average'])
        plt.savefig("Non_Optimized_data_merge_sort.png")

        plt.figure()
        plt.plot(X, cpp_binary_search, 'ob', markerfacecolor='none')
        plt.plot(X, rust_binary_search, 'sr', markerfacecolor='none')
        plt.plot(X, [cpp_binary_search_ave for _ in X], '--b')
        plt.plot(X, [rust_binary_search_ave for _ in X], '--r')
        plt.xlabel('x-axis')
        plt.ylabel('Runtime in nanoseconds') 
        plt.title("Comparison of Rust vs Cpp in Binary Search")
        plt.legend(['Cpp Data', 'Rust Data', 'Cpp Average', 'Rust Average'])
        plt.savefig("Non_Optimized_data_binary_search.png")

    # if arg is passed to python file run else
    else:
        print("\nRun Cpp and Rust files with optimazations (as ns)")

        # Run with optimal build
        os.system("g++ main.cpp -O3 && ./a.out")
        os.system("RUSTFLAGS=-Awarnings cargo run --release --manifest-path rust_version/Cargo.toml")
        for _ in range(size):
            os.system("./a.out")
            os.system("./rust_version/target/release/rust_version")

            with open(cpp_file) as cpp_reader: 
                cpp_data = cpp_reader.readlines()
                cpp_data = [int(line.rstrip()) for line in cpp_data]
                cpp_read_file.append(cpp_data[0])
                cpp_merge_sort.append(cpp_data[1])
                cpp_binary_search.append(cpp_data[2])

                

            with open(rust_file) as rust_reader:
                rust_data = rust_reader.readlines()
                rust_data = [int(line.rstrip()) for line in rust_data]
                rust_read_file.append(rust_data[0])
                rust_merge_sort.append(rust_data[1])
                rust_binary_search.append(rust_data[2])

        X = np.arange(size)

        cpp_read_file_ave = sum(cpp_read_file)/(len(cpp_read_file))
        cpp_merge_sort_ave = sum(cpp_merge_sort)/(len(cpp_merge_sort))
        cpp_binary_search_ave = sum(cpp_binary_search)/(len(cpp_binary_search))

        rust_read_file_ave = sum(rust_read_file)/(len(rust_read_file))
        rust_merge_sort_ave = sum(rust_merge_sort)/(len(rust_merge_sort))
        rust_binary_search_ave = sum(rust_binary_search)/(len(rust_binary_search))

        plt.figure()
        plt.plot(X, cpp_read_file, 'ob', markerfacecolor='none')
        plt.plot(X, rust_read_file, 'sr', markerfacecolor='none')
        plt.plot(X, [cpp_read_file_ave for _ in X], '--b')
        plt.plot(X, [rust_read_file_ave for _ in X], '--r')
        plt.xlabel('x-axis')
        plt.ylabel('Runtime in nanoseconds')
        plt.title("Comparison of Rust vs Cpp in Reading from a File")
        plt.legend(['Cpp Data', 'Rust Data', 'Cpp Average', 'Rust Average'])
        plt.savefig("Optimized_data_read_file.png")

        plt.figure()
        plt.plot(X, cpp_merge_sort, 'ob', markerfacecolor='none')
        plt.plot(X, rust_merge_sort, 'sr', markerfacecolor='none')
        plt.plot(X, [cpp_merge_sort_ave for _ in X], '--b')
        plt.plot(X, [rust_merge_sort_ave for _ in X], '--r')
        plt.xlabel('x-axis')
        plt.ylabel('Runtime in nanoseconds')
        plt.title("Comparison of Rust vs Cpp in Merge Sort")
        plt.legend(['Cpp Data', 'Rust Data', 'Cpp Average', 'Rust Average'])
        plt.savefig("Optimized_data_merge_sort.png")

        plt.figure()
        plt.plot(X, cpp_binary_search, 'ob', markerfacecolor='none')
        plt.plot(X, rust_binary_search, 'sr', markerfacecolor='none')
        plt.plot(X, [cpp_binary_search_ave for _ in X], '--b')
        plt.plot(X, [rust_binary_search_ave for _ in X], '--r')
        plt.xlabel('x-axis')
        plt.ylabel('Runtime in nanoseconds') 
        plt.title("Comparison of Rust vs Cpp in Binary Search")
        plt.legend(['Cpp Data', 'Rust Data', 'Cpp Average', 'Rust Average'])
        plt.savefig("Optimized_data_binary_search.png")


if __name__ == "__main__": 
    sns.set_theme()
    main()