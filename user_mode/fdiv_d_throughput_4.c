
#include <math.h>
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

void write_to_csv(const char* instruction, const char* sequence_length, double cycles_per_instruction) {
    FILE* file = fopen("ThroughputResults.csv", "a");
    fprintf(file, "%s, %s, %f\n", instruction,  sequence_length, cycles_per_instruction);
    fclose(file);
}

int main() {

__asm__ __volatile__("fmov d9, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d10, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d11, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d12, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d13, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d14, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d15, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d16, %0" : : "r" (1)); 
__asm__ __volatile__("fmov d17, %0" : : "r" (1)); 


// Loop for warmup runs

for (int i = 0; i <2; i++) {
   

    // Clear the registers and write the pmu counter in x20
    __asm__ __volatile__("mov x19, 1");
    __asm__ __volatile__("mov x20, 0");
    __asm__ __volatile__("mov x21, 0");

    __asm__ volatile("isb");
    __asm__ __volatile__("mrs x20, pmccntr_el0");

    // Add the instructions to be tested in the loop
    __asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");
__asm__ __volatile__("fdiv d1, d9, d10");
__asm__ __volatile__("fdiv d2, d9, d11");
__asm__ __volatile__("fdiv d3, d9, d13");
__asm__ __volatile__("fdiv d4, d9, d13");

}

    // Get the final value of the pmu counter and write it in x21
    __asm__ __volatile__("mrs x21, pmccntr_el0");
    __asm__ volatile("isb");

    // Calculate the resulting number of cycles and print it out
    uint64_t start_cycles = 0;
    __asm__ __volatile__("mov %0, x20" : "=r" (start_cycles));
    uint64_t end_cycles = 0;
    __asm__ __volatile__("mov %0, x21" : "=r" (end_cycles));
    uint64_t cycles_over_all = end_cycles - start_cycles;
    double cycles_per_instruction = (double)(cycles_over_all / 150.0);
    //double throughput = 1.0 / cycles_per_instruction;
    // double throughput = cycles_per_instruction;
    //int roundedThroughput = round(throughput);
    write_to_csv("fdiv_d", "4", cycles_per_instruction);

    return 0;
}
