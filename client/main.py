import grpc
import snowdrop_pb2
import snowdrop_pb2_grpc



def main():
  with grpc.insecure_channel('localhost:8080') as channel:
    stub = snowdrop_pb2_grpc.EchoStub(channel)
    resp = stub.EchoMe(
      request=snowdrop_pb2.EchoRequest(
        Body="Hey there",
        IDNumber=12
      )
    )
    print(resp.Body)



if __name__ == "__main__":
    main()
