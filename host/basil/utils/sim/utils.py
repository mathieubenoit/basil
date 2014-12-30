#
# ------------------------------------------------------------
# Copyright (c) All rights reserved
# SiLab, Institute of Physics, University of Bonn
# ------------------------------------------------------------
#

def cocotb_makefile(sim_files, top_level = 'tb', test_module='basil.utils.sim.Test' ,sim_host='localhost', sim_port=12345, sim_bus='basil.utils.sim.BasilBusDriver', 
                    end_on_disconnect=True, include_dirs=['../../../device/modules'] ):
    
    mkfile = "SIMULATION_HOST?=%s\nSIMULATION_PORT?=%d\nSIMULATION_BUS?=%s\n" % (sim_host, sim_port, sim_bus)
    
    if(end_on_disconnect):
        mkfile += "SIMULATION_END_ON_DISCONNECT?=1\n"
    
    mkfile += "\n"
      
    mkfile += "VERILOG_SOURCES = %s\n\n" % (" ".join(str(e) for e in sim_files))

    mkfile += "TOPLEVEL = %s\nMODULE   = %s\n\n" % (top_level, test_module)

    mkfile += "EXTRA_ARGS = -D_IVERILOG_ %s \n\n" % (" ".join( '-I'+str(e) for e in include_dirs))

    mkfile += """
export SIMULATION_HOST
export SIMULATION_PORT
export SIMULATION_BUS
export SIMULATION_END_ON_DISCONNECT

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
    """
    
    return mkfile