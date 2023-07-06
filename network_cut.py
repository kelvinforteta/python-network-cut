#!usr/bin/env python

import netfilterqueue


def process_packet(packet):
    print(packet)
    # accept packets
    packet.acceopt()

    # drop packets
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run
