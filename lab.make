CMD_LINE_ARGS=--engine papi --stat PAPI_L2_STM --stat rapl:::PACKAGE_ENERGY:PACKAGE0 --vec-small 128Mi --vec-large 128Mi
include $(ARCHLAB_ROOT)/compile.make

.PHONY: run-submission
run-submission: default

%.exe : %.o ../lab_files/main.o
	$(CXX) $(LDFLAGS) $^ -o $@

